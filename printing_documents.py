from pathlib import Path
import os
import tempfile
import win32api
import win32print
import PyPDF2

pages = 0
files = []

def add_page_count(entry) -> int:
    # Read current file and count pages, add to tally
    file = open(entry, "rb")
    pdfReader = PyPDF2.PdfReader(file)

    return len(pdfReader.pages)


def list_files_scandir(path='.'):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                # Add the filepath to the list to print
                files.append([entry.path, add_page_count(entry)])
            elif entry.is_dir():
                list_files_scandir(entry.path)

 
# Specify the directory path you want to start from
directory_path = 'example_path/files'
if os.path.exists(directory_path):
    print(os.listdir(directory_path))
list_files_scandir(directory_path)

for file in files:
    pages += file[1]


print(f"\nNumber of files to be printed: {len(files)}, pages: {pages}\n")

print = input("Print? y/n\n")
if print == "y":
    print = True
else:
    print = False

# Loop through list and print the files
if print:
    print("Printing...")
    for file in files:
        win32api.ShellExecute (
        0,
        "print",
        str(file),

        win32print.GetDefaultPrinter(),
        ".",
        0
        )