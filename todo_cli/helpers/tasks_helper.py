"""
This module contains all logic pertaining to the Tasks.json file.
"""

from todo_cli.helpers.path_helper import join_paths, path_exists
from todo_cli.helpers.storage_helper import get_storage_directory
from todo_cli.helpers.json_helper import read_json_file, write_json_file


def install_tasks_file():
    """
    Creates the Storage files in the directory that the user specifies.
    """
    storage_directory = get_storage_directory()
    tasks_file_path = join_paths(storage_directory, "tasks.json")
    if not path_exists(tasks_file_path):
        write_json_file(tasks_file_path, [])


def read_tasks_file() -> str:
    """
    This will read the tasks.json file.

    Returns:
        str: The directory to tasks.json file.
    """
    storage_directory = get_storage_directory()
    storage_file = f"{storage_directory}/tasks.json"
    storage_content = read_json_file(storage_file)
    return storage_content


def write_tasks_file(content: list[dict]) -> None:
    """
    This will write content to task file and if the task file doesnt exist
    it will create tasks.json.
    Returns:
        str: The directory to tasks.json file.
    """
    storage_directory = get_storage_directory()
    storage_file = f"{storage_directory}/tasks.json"
    write_json_file(storage_file, content)


def create_task(name: str, date: str) -> dict:
    """
    This will create a new task dictionary and return it.

    args:
        name(str): This is the name of the task
        date(str): The date

    Returns:
        dict: Data for tasks.json file.
    """

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
        print(item["name"], '|', item["date"])
