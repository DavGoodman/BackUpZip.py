# ! python3
from pathlib import Path
import os, zipfile, shutil

p = Path.home()
copy_folder = Path(p / r"PycharmProjects\pythonProject\beginner_stuff")

zips_list = []
for folder in os.listdir(p):
    if folder.startswith("beginner_stuff_") and folder.endswith(".zip"):
        zips_list.append(folder)

number = 1
while True:
    if f"beginner_stuff_{str(number)}.zip" in zips_list:
        number += 1
        continue
    else:
        break

new_zip = zipfile.ZipFile(p / f"beginner_stuff_{str(number)}.zip", "w")

# Walk the folder tree and compress files in each folder
for foldername, subfolders, filenames in os.walk(copy_folder):
    print(f"Adding files in {foldername}...")
    # Add current folder to zip file
    new_zip.write(foldername)

    # Add all files in filenames
    for filename in filenames:
        new_base = os.path.basename(copy_folder) + "_"
        if filename.startswith(new_base) and filename.endswith(".zip"):
            continue  # dont back up the backup zip files

        new_zip.write(os.path.join(foldername, filename))