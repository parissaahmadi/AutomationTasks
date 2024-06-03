import os
import filecmp
import shutil

def delete_duplicates_between_dirs(dir1, dir2):
    for root, dirs, files in os.walk(dir1):
        for name in files:
            file1 = os.path.join(root, name)
            file2 = file1.replace(dir1, dir2)
            if os.path.isfile(file1) and os.path.isfile(file2):
                if filecmp.cmp(file1, file2, shallow=False):
                    if os.path.getmtime(file1) > os.path.getmtime(file2):
                        os.remove(file2)
                        print(f'Deleted duplicate file: {file2}')
                    else:
                        os.remove(file1)
                        print(f'Deleted duplicate file: {file1}')

def delete_duplicates_within_dir(dir):
    checked_files = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            file = os.path.join(root, name)
            for checked_file in checked_files:
                if filecmp.cmp(file, checked_file, shallow=False):
                    if os.path.getmtime(file) > os.path.getmtime(checked_file):
                        os.remove(checked_file)
                        print(f'Deleted duplicate file: {checked_file}')
                    else:
                        os.remove(file)
                        print(f'Deleted duplicate file: {file}')
                    break
            checked_files.append(file)

# Replace 'drive1' and 'drive2' with your actual drive paths
# Comment any function you don't need so that it doesn't run. (Type # at the beginning of the code so that it appears in green.)
delete_duplicates_between_dirs('D:\\', 'E:\\')
delete_duplicates_within_dir('D:\\')
