import os
# specify the path to the directory you want to list
path = "/"
# get a list of all files and directories in the specified path
directory = os.listdir(path)
# print the list of files and directories
for item in directory:
    print(item)