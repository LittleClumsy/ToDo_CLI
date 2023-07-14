"""
This module contains all logic pertaining to the CLI commands
"""
import typer
import uuid
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
    Creates new task.

    args:
        name(str): This is the name of the task
        date(str): The date
    """
    task_uuid = str(uuid.uuid4())
    adding_content(task_uuid, name, date)


@app.command()
def view() -> None:
    """View existing tasks"""
    view_tasks()


@app.command()
def edit(
    id: Annotated[str, typer.Option(prompt=True)],
    field_name: Annotated[str, typer.Option(prompt=True)],
    value: Annotated[str, typer.Option(prompt=True)]
) -> None:
    """
    Edits existing tasks

    args: 
        id(str): This is the uuid of the task
        field_name(str): This is the field you would like to edit
        value(str): The new value for the field name
    """
    if field_name == "UUID":
        print("Invalid field. The UUID can not be edited.")
        raise typer.Exit(code=3)
    elif field_name != "name" and field_name != "date":
        print("That field does not exist! Please select a valid field to edit.")
        raise typer.Exit(code=3)

    content = read_tasks_file()
    for task in content:
        if task['UUID'] == id:
            task[field_name] = value
    write_tasks_file(content)


def adding_content(task_uuid: str, name: str, date: str):
    """
    This function will handle adding a task to the tasks.json file

    args:
        name(str): This is the name of the task
        date(str): The date
    """
    tasks_data = read_tasks_file()
    new_task = create_task(task_uuid, name, date)
    tasks_data.append(new_task)
    write_tasks_file(tasks_data)
