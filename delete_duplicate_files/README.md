# Delete Duplicate files
This Python script is designed to automate the task of identifying and removing duplicate files across two directories, as well as within a single directory. Here's how it works:

### 1. Delete Duplicates Between Two Directories: 
The function `delete_duplicates_between_dirs(dir1, dir2)` takes two directory paths as input. It recursively traverses all files in `dir1` and for each file, it checks if a file with the same name exists in `dir2`. 
If such a file exists and the contents of the two files are identical, the older file is deleted.

### 2. Delete Duplicates Within a Single Directory:
The function `delete_duplicates_within_dir(dir)` takes a directory path as input. It compares every file in the directory with every other file in the same directory. If it finds two files that have the same content, it deletes the older file.

## Usage:
To use this script, you need to replace `'D:\\'` and `'E:\\'` with the actual paths of your directories. Then, run the script. 
It will automatically traverse the files in the specified directories and remove any duplicates it finds, keeping only the most recent copy of each file.

Please note that this script uses the `os`, `filecmp`, and `shutil` libraries, which are part of the Python Standard Library and should be available in any standard Python installation. 
Therefore, no additional package installations are required to run this script.

Remember to always back up your data before running any script that modifies or deletes your files. While this script is designed to only remove duplicate files, it's always a good idea to have a backup just in case. Happy coding!
