import shutil
import pathlib

current_file = pathlib.Path.cwd() / "text.txt"

if current_file.exists():
    print("file is exists")
    current_file.unlink()
    print(shutil.disk_usage("/", encoding="utf-8"))
else:
    print("file is not exists!")
    print("let's create it")
    with open(current_file, "w") as fp:
        fp.write("hi am sameer")
