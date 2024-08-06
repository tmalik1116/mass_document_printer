from pathlib import Path
import os
import tempfile
import win32api
import win32print

for foldernum in range(34): # can be set to anything
    
    path = f"../Example/Folder {foldernum}"

    if os.path.exists(path):
        print(os.listdir(path))

files = []
def list_files_scandir(path='.'):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                files.append(entry.path)
            elif entry.is_dir():
                list_files_scandir(entry.path)
 
# Specify the directory path you want to start from
directory_path = '../Example'
list_files_scandir(directory_path)


print(f"\nNumber of files to be printed: {len(files)}\n")

# Loop through list and print the files
for file in files:
    win32api.ShellExecute (
      0,
      "print",
      str(file),

      win32print.GetDefaultPrinter(),
      ".",
      0
    )

