"""
This module will contain all the logic to pertaining to the installation of files needed for the program
"""
from helpers.os_helper import join_paths, path_exists

def install_storage_file():
    """
    Creates the Storage files in the directory that the user specifies.
    """
    directory_path = input("Enter the directory path where you want to install the file: ")

    file_to_install = "tasks.json"
    file_path = join_paths(directory_path, file_to_install)

    if not path_exists(directory_path):
        print("This path doesn't exist.")
    elif path_exists(file_path):
        print("This file already exists in this directory.")
    else:
        with open(file_path, 'w'):
            pass