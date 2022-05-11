import os
import shutil



#If you'd like to test add yours.
home_path = "/home/valera/"
path_tests = "/home/valera/tests/"
path_pytests = "/home/valera/pytest/csv/"
garbage_path = "/home/valera/garbage/"
path_downloads = "/home/valera/Downloads/"



#Function checks if directory in given path already exists.
#If not, creates.
def dir_exists(path):
    exist_check = os.path.exists(path)
    if exist_check is True:
        print("Directory already exists")
    else:
        os.mkdir(garbage_path)
        print(f"Directory created: {garbage_path}")

"""
#Copies exact types of files from source path directory to the target:
def copy_exact_contents(source, destination):
    source_list = os.listdir(source)
    for file in source_list:
        if file.endswith('.csv'):
            shutil.copyfile(os.path.join(source, file), os.path.join(destination, file))
        elif file.endswith('.xls'):
            shutil.copyfile(os.path.join(source, file), os.path.join(destination, file))
        elif file.endswith('.xlsx'):
            shutil.copyfile(os.path.join(source, file), os.path.join(destination, file))
        else:
            continue
"""

#Copies '.txt' files from source path directory to the target:
def copy_contents_txt(source, destination):
    source_list = os.listdir(source)
    for file in source_list:
        if file.endswith('.txt'):
            destination_contents = os.listdir(destination)
            if file not in destination_contents:
                shutil.copyfile(os.path.join(source, file), os.path.join(destination, file))
        else:
            continue

#'copy_contents_txt' test:
#copy_contents_txt(path_pytests, garbage_path)
#garbage_contents = os.listdir(garbage_path)



#Copies only files were not copied before:
def only_new_copy(source, destination):
    source_contents = os.listdir(source)
    destination_contents = os.listdir(destination)
    for file in source_contents:
        if file in destination_contents:
            continue
        else:
            copy_contents_txt(source, destination)

#Prints items in destination folder:
def dest_cont_list(destination):
    for item in os.listdir(destination):
        print(item)

#Lists directories under 'path' and adds them to 'dirs_list':
def scan_dir(path):
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_dir():
                dirs_list.append(path + entry.name + "/")
            else:
                continue

#Recursively lists directories added by scan_dir(path) to dirs_list:
def deep_scan(dirs_list):
    for item in dirs_list:
        scan_dir(item)



#Tests:
dirs_list = []
dir_exists(garbage_path)
scan_dir(home_path)

#This block allows you to avoid premature termination of the program, in case of detection of an inaccessible directory:
#Or you may try to execute program using 'sudo' to avoid an error.
try:
    deep_scan(dirs_list)
except PermissionError:
    print('Permission denied')
#Files from hidden directories are also copied:
for i in dirs_list:
    print(i)
    try:
        only_new_copy(i, garbage_path)
    except PermissionError:
        print('Permission denied')

print('List of files were found:')
dest_cont_list(garbage_path)


