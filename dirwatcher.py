#!/usr/bin/env python
import sys, getopt, os, time, magic, shutil
from datetime import datetime, timedelta

path_to_watch = ""
folder_counter = 1
useless_folder_name = "Minimalism"
ignore_file_name = ".DS_Store"

def main(argv):
    """"
    Main Function
    """
    global path_to_watch
    try:
      opts, args = getopt.getopt(argv,"hd:",["dir="])
    except getopt.GetoptError:
      print 'dirwatcher.py -d <directory>'
      sys.exit(2)
    for opt, arg in opts:
     if opt == '-h':
         print 'dirwatcher.py -d <directory>'
         sys.exit()
     elif opt in ("-d", "--dir"):
         path_to_watch = arg
     else:
         print 'dirwatcher.py -d <directory>'
         sys.exit()

    if(os.path.exists(path_to_watch)):
        os.chdir(path_to_watch)
        clearFolders()
        organizeFiles()

def organizeFiles():
    """"
    Organize the files by type and manage folder structure
    """
    global folder_counter
    global path_to_watch
    files = dict ([(os.path.abspath(f),f) for f in os.listdir(path_to_watch)])
    for fp in files:
        if(os.path.isfile(fp)):
            fn = files.get(fp)
            try:
                type = magic.from_file(fp, mime=True).replace("application/","").replace("/","-")
            except:
                print "Exception in magic for: "+fn
            type = filterType(type,fn.lower())
            createTypeFolder(type, fn, fp)



def clearFolders():
    """"
    Check for empty folders and delete them if they are empty
    """
    global path_to_watch
    global ignore_file_name
    files = dict ([(os.path.abspath(f),f) for f in os.listdir(path_to_watch)])
    for fp in files:
        try:
            if(os.path.exists(fp) and os.path.isdir(fp)):
                ff = os.listdir(fp)
                if(len(ff) <= 1 and ignore_file_name in ff):
                    shutil.rmtree(fp)

        except:
            print "Exception for :"+fp


def minimalism():
    """"
    Check for useless files and move them to different folder for inspection
    """
    global ignore_file_name
    for root,d_names,f_names in os.walk(path_to_watch):
    	for f in f_names:
            if(not ignore_file_name in f):
                file_path = os.path.join(root, f)
                useful = checkUseful(file_path)
                if(not useful):
                    if(not os.path.exists(path_to_watch+"/"+useless_folder_name)):
                        os.mkdir(path_to_watch+"/"+useless_folder_name)
                    try:
                        shutil.move(file_path, path_to_watch+"/"+useless_folder_name)
                    except:
                        print "Exception for :"+file_path



def createTypeFolder(type, file_name, file_path):
    """"
    Creates a Folder for the filetype passed.
    """
    global folder_counter
    new_path = "{}/{}".format(path_to_watch,type)
    try:
        if(not os.path.exists(new_path)):
            os.mkdir(new_path)
            folder_counter = folder_counter + 1
        shutil.move(file_path, new_path)
    except:
        print "Exception for :"+file_path

def checkUseful(file_path):
    """"
    Return the last time a file was opened / used
    """
    stat = os.stat(file_path)
    file_time = datetime.fromtimestamp(stat.st_mtime)
    days_ago = datetime.now() - timedelta(days=90)

    print("{} - {}".format(file_time,days_ago))
    if file_time < days_ago:
        return 0
    return 1

def filterType(type,name):
    """"
    Define File Type
    """
    if(".conf" in name):
        type = "Configs"
    elif(".sql" in name):
        type = "SQLs"
    elif(".dmg" in name):
        type = "Installers"
    elif("image" in type) :
        type = "Images"
    elif("zip" in type) :
        type = "Zips"
    elif("pdf" in type) :
        type = "PDFs"
    elif("video" in type) :
        type = "Videos"
    elif("text-plain" in type or "msword" in type):
        type = "Documents"
    elif("sheet" in type):
        type = "Sheets"
    elif("calendar" in type):
        type = "Calendars"
    else: type = "Other"

    return type

if __name__ == '__main__':
    main(sys.argv[1:])
