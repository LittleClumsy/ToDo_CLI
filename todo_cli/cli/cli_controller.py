"""
This module contains all logic pertaining to the CLI commands
"""
import csv
import uuid
from enum import Enum
from typing import List
import pandas as pd

from tabulate import tabulate
from rich.console import Console
from rich.table import Table

import typer
from typing_extensions import Annotated
from todo_cli.helpers.tasks_helper import (
    read_tasks_file,
    create_task,
    write_tasks_file,
    delete_task
)
from todo_cli.config.config_controller import write_config_file, read_config_file
from todo_cli.helpers.json_helper import write_json_file


app = typer.Typer()
delete = typer.Typer()
console = Console()

app.add_typer(delete, name="delete")


class FieldName(str, Enum):
    """
    This class contains the possible field names for tasks
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


class Formats(str, Enum):
    """
    This class contains the different file types for export function.
    """
    JSON = "json"
    CSV = "csv"


class DisplayTypes(str, Enum):
    """
    This class contains the different display options.
    """
    TABLE = "table"
    CSV = "csv"
    RICH = "rich"


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


def view_tabulate(tasks: dict | list) -> None:
    """
    This function will view tasks in table format.

    args:
        tasks: These are the tasks in your tasks.json file.
    """
    headers = ["UUID", "name", "date", "priority"]

    task_rows = [[task["UUID"], task["name"],
                  task["date"], task["priority"]]for task in tasks]
    table = tabulate(task_rows, headers, tablefmt="rounded_grid")
    print(table)


def view_csv(tasks: dict | list, delimiter: str) -> None:
    """
    This function will view tasks in csv format.

    args:
        tasks: These are the tasks in your tasks.json file.
        delimeter: This will replace the comma in your output.
    """
    df = pd.DataFrame(tasks)
    print(df.to_csv(index=False, sep=delimiter))


def view_rich(tasks: dict | list) -> None:
    """
    This function will view tasks in table format.

    args:
        tasks: These are the tasks in your tasks.json file.
    """
    table = Table(title="Tasks")
    table.add_column("UUID", style="cyan", no_wrap=True)
    table.add_column("Name", style="magenta")
    table.add_column("Date", style="green")
    table.add_column("Priority", style="red")
    for task in tasks:
        table.add_row(*list(task.values()))
    console.print(table)


@app.command()
def view() -> None:
    """
    This function will view your tasks
    """
    tasks = read_tasks_file()
    config_file = read_config_file()

    if config_file != {}:
        display_type = config_file["display_type"]
        delimiter = config_file["delimiter"]

        if display_type == "table":
            view_tabulate(tasks)
        elif display_type == "csv":
            view_csv(tasks, delimiter)
        elif display_type == "rich":
            view_rich(tasks)
    else:
        view_rich(tasks)


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


@delete.command("one")
def delete_one(task_id: List[str] = typer.Argument(None)) -> None:
    """
    This function will allow you to delete a single task.
    """
    if task_id is None or len(task_id) == 0:
        typer.echo("Please provide an ID")
        raise typer.Exit(code=3)
    if len(task_id) > 1:
        typer.echo("Can not delete more than 1 task at a time.")
        raise typer.Exit(code=3)

    delete_task(task_id)


@delete.command("many")
def delete_many(task_id: List[str] = typer.Argument(None)) -> None:
    """
    This function will allow you to delete multiple tasks.
    """
    if task_id is None or len(task_id) <= 1:
        print("Please provide at least 2 task id's to delete.")
        raise typer.Exit(code=3)

    delete_task(task_id)


def export_to_csv_file(file: str, content: list | dict):
    """
    This function will export data to file in csv format.

    Args:
        file (str): This is the target file to write data to.
    """
    with open(file, mode='w', newline='', encoding="utf-8") as target_file:
        writer = csv.writer(target_file)
        writer.writerow(['UUID', 'name', 'date', 'priority'])
        for task in content:
            writer.writerow([task['UUID'], task['name'],
                            task['date'], task['priority']])


@app.command()
def export(file_format: Annotated[Formats,
                                  typer.Option(case_sensitive=False, prompt=True)],
           file: Annotated[str, typer.FileTextWrite, typer.Option(prompt=True)]):
    """
    This function will export your data to either a JSON or CSV format

    args:
        file_format(str): This is the format in which you would like to export the file.
        file(str): This is the file you would like to export your data to.
    """
    content = read_tasks_file()

    if file_format == Formats.JSON:
        write_json_file(file, content)
    elif file_format == Formats.CSV:
        export_to_csv_file(file, content)

    print(f"File exported as .{file_format} file.")


@app.command()
def config(display_type: Annotated[DisplayTypes,
                                   typer.Option(case_sensitive=False, prompt=True)]) -> None:
    """
    View existing tasks in either csv or tablulated.
    """
    if display_type == DisplayTypes.CSV:
        delimiter = typer.prompt("Enter delimiter:", default=",")
    else:
        delimiter = "null"

    write_config_file({"display_type": f"{display_type}",
                       "delimiter": f"{delimiter}", })
