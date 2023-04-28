"""
This module contains all logic pertaining to the Tasks.json file.
"""

from todo_cli.config.config_controller import read_config_file
from todo_cli.helpers.json_helper import read_json_file, write_json_file


def read_tasks_file() -> str:
    """
    This will read the tasks.json file.

    Returns:
        str: The directory to tasks.json file.
    """
    config = read_config_file()
    storage_path = config["data_storage"]
    storage_file = f"{storage_path}/tasks.json"
    storage_content = read_json_file(storage_file)

    return storage_content


def write_tasks_file(content: list[dict]) -> None:
    """
    This will write content to task file and if the task file doesnt exist
    it will create tasks.json.
    Returns:
        str: The directory to tasks.json file.
    """
    config = read_config_file()
    storage_path = config["data_storage"]
    storage_file = f"{storage_path}/tasks.json"
    write_json_file(storage_file, content)



def create_task() -> dict:
    """
    This will create a new task dictionary and return it.
    Returns:
        dict: Data for tasks.json file.
    """

    name = input("Enter Name: ")
    date = input("Enter date: ")

    new_task = {
        "name": name,
        "date": date
    }

    return new_task


def view_tasks():
    """
    This will allow user to view their existing tasks.
    """
    tasks_data = read_tasks_file()
    for item in tasks_data:
        print(item["name"],'|',item["date"])
