"""
This module contains all logic pertaining to the Tasks.json file.
"""
from typing import List
import typer

from todo_cli.helpers.path_helper import join_paths, path_exists
from todo_cli.helpers.storage_helper import get_storage_directory
from todo_cli.helpers.json_helper import read_json_file, write_json_file


def install_tasks_file() -> bool:
    """
    Creates the tasks.json file if it does not exist.

    Returns:
        bool: True if the file was created, False if it already exists.

    Raises:
        FileNotFoundError: If the application cannot create the tasks file.
        TypeError: If you you try to write a value to a JSON file that is not of
            type dictionary or list.
    """
    storage_directory = get_storage_directory()
    tasks_file_path = join_paths(storage_directory, "tasks.json")
    if not path_exists(tasks_file_path):
        write_json_file(tasks_file_path, [])
        return True
    return False


def read_tasks_file() -> str:
    """
    This will read the tasks.json file.

    Returns:
        str: The data from tasks.json file.
    """
    storage_directory = get_storage_directory()
    storage_file = f"{storage_directory}/tasks.json"
    storage_content = read_json_file(storage_file)
    return storage_content


def write_tasks_file(content: list[dict]) -> None:
    """
    This will write content to task file and if the task file doesnt exist
    it will create tasks.json.

    Args:
        content (list[dict]): The data to write to the tasks.json file.
    """
    storage_directory = get_storage_directory()
    storage_file = f"{storage_directory}/tasks.json"
    write_json_file(storage_file, content)


def create_task(task_uuid: str, name: str, date: str, priority: str) -> dict:
    """
    This will create a new task dictionary and return it.

    args:
        name(str): This is the name of the task
        date(str): The date

    Returns:
        dict: a singular task dictionary.
    """

    new_task = {
        "UUID": task_uuid,
        "name": name,
        "date": date,
        "priority": priority
    }

    return new_task


def validate_task_ids(task_ids: List[str], content: List[dict]) -> bool:
    """
    Validate if the provided task IDs exist in the task list.
    """
    valid_tasks = [task["UUID"] for task in content]
    return all(task_id in valid_tasks for task_id in task_ids)


def delete_task(task_ids: List[str]) -> None:
    """
    This function will delete a task based on the task id(s) provided
    """
    content = read_tasks_file()
    if not validate_task_ids(task_ids, content):
        print("Provided ID(s) could not be found")
        raise typer.Exit(code=3)

    if not typer.confirm("Are you sure you want to delete this task?"):
        print("Not deleting task.")
        raise typer.Exit(code=0)
    content = [task for task in content if task['UUID'] not in task_ids]
    write_tasks_file(content)
    print(f"Deleted task with ID(s): {task_ids}")
