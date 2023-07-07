"""
This module contains all logic pertaining to the CLI commands
"""
import typer
from typing_extensions import Annotated
from todo_cli.helpers.tasks_helper import (
    read_tasks_file,
    create_task,
    write_tasks_file,
    view_tasks
)


app = typer.Typer()


@app.command()
def create(
    name: Annotated[str, typer.Option(prompt=True)],
    date: Annotated[str, typer.Option(prompt=True)]
) -> None:
    """
    Creates new task

    args:
        name(str): This is the name of the task
        date(str): The date
    """
    adding_content(name, date)


@app.command()
def view() -> None:
    """View existing tasks"""
    view_tasks()


def adding_content(name: str, date: str):
    """
    This function will handle adding a task to the tasks.json file

    args:
        name(str): This is the name of the task
        date(str): The date
    """
    tasks_data = read_tasks_file()
    new_task = create_task(name, date)
    tasks_data.append(new_task)
    write_tasks_file(tasks_data)
