"""
This module will contain all the logic to pertaining to the installation of files needed
for the program
"""
from todo_cli.helpers.os_helper import join_paths, path_exists
from todo_cli.helpers.json_helper import write_json_file
from todo_cli.config.config_controller import read_config_file, write_config_file


def install_storage_file():
    """
    Creates the Storage files in the directory that the user specifies.
    """

    valid_path_entered = False
    while not valid_path_entered:
        directory_path = input(
            "Enter the directory path where you want to install the file: ")

        file_to_install = "tasks.json"
        file_path = join_paths(directory_path, file_to_install)

        if not path_exists(directory_path):
            print("This path doesn't exist.")
        elif path_exists(file_path):
            print("This file already exists in this directory.")
        else:
            valid_path_entered = True

    write_json_file(file_path, [])
    config = read_config_file()
    config["data_storage"] = directory_path
    write_config_file(config)
