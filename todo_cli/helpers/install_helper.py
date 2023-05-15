"""
This module will contain all the logic to pertaining to the installation of files needed
for the program
"""
from todo_cli.helpers.os_helper import join_paths, path_exists
from todo_cli.helpers.json_helper import write_json_file
from todo_cli.config.config_controller import get_config_directory


def install_storage_file():
    """
    Creates the Storage files in the directory that the user specifies.
    """
    config_directory = get_config_directory()
    tasks_file_path = join_paths(config_directory, "tasks.json")
    if not path_exists(tasks_file_path):
        write_json_file(tasks_file_path, [])
