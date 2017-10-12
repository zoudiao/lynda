import os
import shutil
from os import path
from shutil import make_archive
from zipfile import ZipFile


def main():
    #make a duplicate of an exiting file
    if path.exists("textfile.txt"):
        #get the path to the file in the current directory
        src = path.realpath("textfile.txt")

        #separate the path part from the filename
        head,tail = path.split(src)
        print "path:"+head
        print "file:"+tail

        #let's make a backup copy by appending "bak" to the name
        dst = src +".bak"
        #now use the shell to make a copy of the file
        shutil.copy(src,dst)

        #copy over the permissions,modification times,and other info
        shutil.copystat(src,dst)

        #rename the original file
        os.rename("textfile.txt","newfile.txt")

        #now put things into a ZIP archive
        root_dir,tail = path.split(src)
        shutil.make_archive("archive","zip",root_dir)

        #more fine-grained control over ZIP files
        with ZipFile("testzip.zip","w") as newzip:
            newzip.write("newfile.txt")
            newzip.write("textfile.txt.bak")


if __name__ == '__main__':
    main()