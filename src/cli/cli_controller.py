"""
This module contains all logic pertaining to the CLI commands
"""

from helpers.tasks_helper import read_tasks_file, create_task, write_tasks_file, view_tasks




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
    elif cli_args[0] == "view":
        view_tasks()


def adding_content():
    """
    This function will handle adding a task to the tasks.json file
    """
    tasks_data = read_tasks_file()
    new_task = create_task()
    tasks_data.append(new_task)
    write_tasks_file(tasks_data)


