import os
from os.path import join

word = "file"
ext = ".txt"
path = "./"
for i in range(1, 11):
    full_path = join(path, i)
    with open(full_path, "w") as cr:
        cr.write(f"{word}{i}{ext}")
    print("file created!")
