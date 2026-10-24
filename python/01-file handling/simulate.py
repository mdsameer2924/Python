import os
from os.path import isdir, join

path = "../6md/"


print(os.listdir(path))
for i in os.listdir(path):
    fullpath = join(path, i)
    if isdir(fullpath):
        print(f"folder: {i}")
    else:
        print(f"file: {i}")
