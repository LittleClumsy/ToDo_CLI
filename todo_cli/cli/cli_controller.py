"""
This module contains all logic pertaining to the CLI commands
"""
import uuid
from enum import Enum
from tabulate import tabulate
import typer
from typing_extensions import Annotated
from todo_cli.helpers.tasks_helper import (
    read_tasks_file,
    create_task,
    write_tasks_file
)


app = typer.Typer()


class FieldName(str, Enum):
    """
    This clas contains the possible field names for tasks
    """
    NAME = "name"
    DATE = "date"
    PRIORITY = "priority"


class Priority(str, Enum):
    """
    This class contains the different priority fields for tasks
    """
    VERY_HIGH = "Very High"
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"
    VERY_LOW = "Very Low"


@app.command()
def create(
    name: Annotated[str, typer.Option(prompt=True)],
    date: Annotated[str, typer.Option(prompt=True)],
    priority: Annotated[Priority,
                        typer.Option(case_sensitive=False, prompt=True)]
) -> None:
    """
    Creates new task.

    args:
        name(str): This is the name of the task
        date(str): The date
        priority_field(str): The level of priority of the task
    """
    task_uuid = str(uuid.uuid4())

    adding_content(task_uuid, name, date, priority)


@app.command()
def view() -> None:
    """View existing tasks in the form of a table"""
    tasks = read_tasks_file()
    headers = ["UUID", "name", "date", "priority"]
    task_rows = [[task["UUID"], task["name"],
                  task["date"], task["priority"]]for task in tasks]
    table = tabulate(task_rows, headers, tablefmt="rounded_grid")
    print(table)


@app.command()
def edit(
    task_id: Annotated[str, typer.Option(prompt=True)],
    field_name: Annotated[FieldName, typer.Option(prompt=True)],
    value: Annotated[str, typer.Option(prompt=True)]
) -> None:
    """
    Edits existing tasks

    args: 
        id(str): This is the uuid of the task
        field_name(str): This is the field you would like to edit
        value(str): The new value for the field name
    """

    all_priority_options = [element.value for element in Priority]

    if field_name == "priority" and value not in all_priority_options:
        print("This is an invalid priority value.")
        raise typer.Exit(code=3)

    content = read_tasks_file()
    for task in content:
        if task['UUID'] == task_id:
            task[field_name] = value
    write_tasks_file(content)


def adding_content(task_id: str, name: str, date: str, priority: str):
    """
    This function will handle adding a task to the tasks.json file

    args:
        task_id(str): This is the UUID of the task 
        name(str): This is the name of the task
        date(str): The date
        Priority_field(str): The level of priority for the task
    """
    tasks_data = read_tasks_file()
    new_task = create_task(task_id, name, date, priority)
    tasks_data.append(new_task)
    write_tasks_file(tasks_data)
