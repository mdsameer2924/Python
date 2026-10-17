import os

folder = "/home/sameer/Documents/Work/Learning/python/python/file handling/stores/"
target_file_extension = input("Enter the file extension to delete all related file:  ")
for file_name in os.listdir(folder):
    full_path = os.path.join(folder, file_name)
    print(full_path)
    if file_name.endswith(target_file_extension.strip()):
        os.remove(full_path)
        print(f"file: {file_name} successfully deleted!.")
    else:
        print("File does not exist!.")
