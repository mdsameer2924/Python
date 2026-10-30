import shutil

s = shutil.which("cmatrix")
if s:
    print("exist")
else:
    print("not exist")
