import os
import shutil
import time

def main():
    deleted_folders_count = 0
    deleted_files_count = 0

    path = "N:\PYTHON\C99\Project"

    days =30

    seconds = time.time()-(days*24*60*60)

    if os.path.exists(path):
       for root_folder,folder,files in os.walk(path):
           if seconds >= get_file_or_folder_age(root_folder):
                remove_folder(root_folder) 
                deleted_folders_count += 1
                break
           else:
                for folder in folder: 
                    folder_path = os.path.join(root_folder, folder) 
                    if seconds >= get_file_or_folder_age(folder_path): 
                        remove_folder(folder_path) 
                        deleted_folders_count += 1

                for files in files: 
                    files_path = os.path.join(root_folder, files) 
                    if seconds >= get_file_or_folder_age(files_path): 
                        remove_files(files_path) 
                        deleted_files_count += 1

    else:
         print(f'"{path}"is not found')
         deleted_files_count += 1

    print(f"Total Folders Deleted = {deleted_folders_count}")
    print(f"Total Filess Deleted = {deleted_files_count}")

def remove_folder(path):
    if not shutil.rmtree(path):
        print(f"{path} is sucessfully removed")


    else:
        print(f" unable to delete"+path)

def remove_files(path):
    if not shutil.rmtree(path):
        print(f"{path} is sucessfully removed")


    else:
        print(f" unable to delete"+path)


           
def get_file_or_folder_age(path):
    ctime=os.stat(path).st_ctime
    return ctime

if __name__ == '__main__':
    main()


  

