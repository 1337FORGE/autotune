#!/usr/bin/env python3

# This script is part of my AutoTune project, which is a collection of scripts that automate some of my repetitive tasks.
# This script will automate creating A to Z folder structure inside a folder with current year.
# You can find this script on GitHub https://github.com/sacredbeacon/autotune


#Libraries
import os
import datetime


# Banner
banner = """
_______       _____      _____                    
___    |___  ___  /________  /____  _____________ 
__  /| |  / / /  __/  __ \  __/  / / /_  __ \  _ |
_  ___ / /_/ // /_ / /_/ / /_ / /_/ /_  / / /  __/
/_/  |_\__,_/ \__/ \____/\__/ \__,_/ /_/ /_/\___/ 
                                    AutoAZ v1.0
"""


# Printing Banner
print(banner)


# Detecting Operating System
if os.name == 'nt':
    os_type = 'Windows'
elif os.name == 'posix':
    os_type = 'Linux'
else:
    print("OS not supported")
    exit()


# Check if a folder with current year exists
if os_type == 'Windows':
    if os.path.exists(str(datetime.datetime.now().year)):
        print("Folder with current year already exists")
        exit()
elif os_type == 'Linux':
    if os.path.exists('./' + str(datetime.datetime.now().year)):
        print("Folder with current year already exists")
        exit()
else:
    print("Creating folder with current year")


# Creating Main Folder with current year
year = datetime.datetime.now().year
if os_type == 'Windows':
    os.mkdir(str(year))
elif os_type == 'Linux':
    os.mkdir('./' + str(year))


# Creating Sub Folders with A to Z inside Main Folder
for i in range(65, 91):
    if os_type == 'Windows':
        os.mkdir(str(year) + '/' + chr(i))
    elif os_type == 'Linux':
        os.mkdir('./' + str(year) + '/' + chr(i))


# Printing the folders path
print("Folders created successfully")
if os_type == 'Windows':
    print("Path: " + os.getcwd() + '\\' + str(year))
elif os_type == 'Linux':
    print("Path: " + os.getcwd() + '/' + str(year))
else:
    print("OS not supported")
    exit()
