"""
This module contains all logic pertaining to the CLI commands
"""

from config.config_controller import read_config_file
from helpers.json_helper import write_json_file, read_json_file

def handle_cli_args(cli_args: list[str]) -> None:
    """
    This function will take redirect to the corresponding function for the CLI arg.

    Args:
        cli_args (list[str]): The CLI args passed.   
    """
    if len(cli_args) < 1:
        print("This should be the help command.")
    elif cli_args[0] == "create":
        adding_content()

def adding_content():
    """
    This function will handle adding a task to the tasks.json file
    """
    config = read_config_file()
    storage_path = config["data_storage"]
    storage_file = f"{storage_path}/tasks.json"

    tasks_data = read_json_file(storage_file)

    name = input("Enter Name: ")
    date = input("Enter date: ")

    new_task = {
        "name": name,
        "date": date
    }

    tasks_data.append(new_task)

    write_json_file(storage_file, tasks_data)