"""
This module contains all logic pertaining to the CLI commands
"""
import typer
from todo_cli.helpers.tasks_helper import read_tasks_file, create_task, write_tasks_file, view_tasks

app = typer.Typer()

@app.command()
def create() -> None:
    """Creates new task"""
    adding_content()


@app.command()
def view() -> None:
    """View existing tasks """
    view_tasks()


def adding_content():
    """
    This function will handle adding a task to the tasks.json file
    """
    tasks_data = read_tasks_file()
    new_task = create_task()
    tasks_data.append(new_task)
    write_tasks_file(tasks_data)
