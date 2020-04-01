# dirwatcher
*Directory watcher for people who care about order and organization* 

Everyone knows this feeling...the moment you look at your Downloads folder or your Desktop and it's all unordered and unmanaged clutter.
For years and months I had gone by doing it myself and maintaining the order that I thought was acceptable. But today was going to be a different day!
I decided to put a stop to it! Never again.

This little script manages all files in a directory and sorts them by filetype:

 - Images
 - Videos
 - Pdfs
 - Sql files
 - Installers (mac)
 - Configs
 - Documents
 - Sheets
and other.

Also it takes care of deleting empty folders as well.
A minimalist approach is also included where older files get moved to a dedicated folder for you to check, but the option needs to be invoked in the code for now. We shall see about that.

Use a crontab:

    crontab -e
   Then add the following:
   

    * * * * * python /path/to/dirwatcher.py -d path/to/directory

## Here is some inspiration

> Clutter is nothing more than postponed decisions
> Organizing is a journey, not a destination
> For every minute spent organizing, an hour is earned
> Bottom line is, if you do not use it or need it, it’s clutter, and it needs to go.
> The only difference between a mob and a trained army is organization.



