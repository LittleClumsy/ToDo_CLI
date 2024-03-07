"""
This module will contain the tests for the cli_controller module
"""
import csv
from json import load, dump
from os import path
from io import StringIO
from contextlib import redirect_stdout
import pandas as pd

from tabulate import tabulate
from rich.table import Table
from rich.console import Console

import pytest
from typer.testing import CliRunner


from tests.test_helpers import (
    clean_up,
    STORAGEDIR,
    setup_test_directory,
    setup_test_config,
    setup_test_tasks
)
from todo_cli.cli.cli_controller import (
    app,
    view_tabulate,
    view_csv
)
from todo_cli.config.config_controller import (read_config_file)


runner = CliRunner()


@pytest.fixture(autouse=True)
def run_before_and_after_tests():
    """
    This function will run the clean_up function before and after the tests.
    """
    setup_test_directory()
    setup_test_config()
    setup_test_tasks()
    yield
    clean_up()


def test_create_command():
    """
    This will test the create command
    """
    result = runner.invoke(app, ["create"], input="laundry\n2023\nLow\n")
    assert result.exit_code == 0

    tasks_file = path.join(STORAGEDIR, "tasks.json")
    file_result = []
    with open(tasks_file, "r", encoding="utf-8") as file:
        file_result = load(file)
    assert file_result[0].get("UUID") is not None
    assert file_result[0].get("name") == "laundry"
    assert file_result[0].get("date") == "2023"
    assert file_result[0].get("priority") == "Low"


def test_view_tabulate_command():
    """
    This will test the tabulate view command.
    """
    task = [
        {"UUID": "abcd1234",
                 "name": "Run",
                 "date": "2022",
                 "priority": "High"
         }
    ]

    f = StringIO()
    with redirect_stdout(f):
        view_tabulate(task)

    result = f.getvalue()

    expected_table = tabulate(
        [
            ["abcd1234", "Run", "2022", "High"]
        ],
        headers=["UUID", "name", "date", "priority"],
        tablefmt="rounded_grid"
    )
    assert result == (expected_table + "\n")


def test_view_csv_command():
    """
    This will test the csv view command.
    """
    task = [
        {"UUID": "abcd1234",
         "name": "laundry",
         "date": "2018",
         "priority": "Low"
         }
    ]
    f = StringIO()
    with redirect_stdout(f):
        view_csv(task, ',')

    result = f.getvalue()

    df = pd.DataFrame(task)
    expected_csv = df.to_csv(index=False, sep=',')

    assert result == (expected_csv + '\n')


def create_expected_output(display_type, data):
    """
    This will generate the expected output for our view test.
    """
    if display_type == "table":
        return tabulate(data, headers=["UUID", "name", "date", "priority"], tablefmt="rounded_grid")
    if display_type == "csv":
        return "UUID|name|date|priority\n" + "|".join(data[0])
    if display_type == "rich":
        table = Table(title="Tasks")
        for column in ["UUID", "Name", "Date", "Priority"]:
            table.add_column(column)
        for row in data:
            table.add_row(*row)
        f = StringIO()
        with redirect_stdout(f):
            console = Console()
            console.print(table)
    return f.getvalue()


@pytest.mark.parametrize("display_type,delimiter,data",  [
    ("table", "null", [["abcd1234", "Walk", "2022", "Medium"]]),
    ("csv", "|", [["abcd1234", "Walk", "2022", "Medium"]]),
    ("rich", "null", [["abcd1234", "Walk", "2022", "Medium"]])
])
def test_view_with_different_display_types(display_type, delimiter, data):
    """
    This will test our view function for all format type options.
    """
    setup_test_config({"display_type": display_type, "delimiter": delimiter})
    setup_test_tasks(
        '''[{"UUID": "abcd1234", "name": "Walk", "date": "2022", "priority": "Medium"}]''')

    expected_output = create_expected_output(display_type, data)

    result = runner.invoke(app, ["view"])
    assert result.exit_code == 0
    assert result.stdout.rstrip('\n') == expected_output.rstrip('\n')


def test_edit_command():
    """
    This will test the edit command
    """
    tasks_file = path.join(STORAGEDIR, "tasks.json")

    with open(tasks_file, "w", encoding="utf-8") as file:
        dump(
            [
                {"UUID": "abcd1234",
                 "name": "laundry",
                 "date": "2018",
                 "priority": "Low"
                 }
            ], file
        )

    result = runner.invoke(app, ["edit"], input="abcd1234\ndate\n2023\n")
    assert result.exit_code == 0

    file_result = []
    with open(tasks_file, "r", encoding="utf-8") as file:
        file_result = load(file)
    assert file_result == [
        {"UUID": "abcd1234", "name": "laundry", "date": "2023", "priority": "Low"}]


def test_edit_command_invalid_priority_field():
    """This will test an invalid priority field entry"""
    result = runner.invoke(
        app,
        [
            "edit",
            "--task-id",
            "abcd1234",
            "--field-name",
            "priority",
            "--value",
            "2023"
        ]
    )
    assert result.exit_code == 3
    assert result.stdout == "This is an invalid priority value.\n"


def test_delete_one_no_id():
    """
    This will test the delete function when there is no id provided.
    """
    result = runner.invoke(app, ["delete", "one"])
    assert result.exit_code == 3
    assert result.stdout == "Please provide an ID\n"


def test_delete_one_multiple_ids():
    """
    This will test the delete function when there are too many ids provided.
    """
    result = runner.invoke(app, ["delete", "one", "123", "456"])
    assert result.exit_code == 3
    assert "Can not delete more than 1 task at a time." in result.stdout


def test_delete_many_no_id():
    """
    This will test the delete function when there is no id provided.
    """
    result = runner.invoke(app, ["delete", "many"])
    assert result.exit_code == 3
    assert "Please provide at least 2 task id's to delete." in result.stdout


def test_export_to_csv_file():
    """
    This will test the export to csv file function.
    """
    tasks_file = path.join(STORAGEDIR, "tasks.json")

    with open(tasks_file, "w", encoding="utf-8") as file:
        dump(
            [
                {"UUID": "abcd1234",
                 "name": "laundry",
                 "date": "2018",
                 "priority": "Low"
                 }
            ], file
        )

    result = runner.invoke(app, ["export"], input="csv\nfile.csv\n")
    assert result.exit_code == 0

    file_result = ''
    with open('./file.csv', newline='', encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            file_result += ','.join(row) + '\n'
    assert file_result == "UUID,name,date,priority\nabcd1234,laundry,2018,Low\n"


def test_config_table():
    """
    This will test the config function if display_type is table.
    """
    runner.invoke(app, ["config"], input="table")
    config_result = read_config_file()
    assert config_result == {"delimiter": "null", "display_type": "table"}


def test_config_csv():
    """
    This will test the config function if display_type is csv.
    """
    runner.invoke(app, ["config"], input="csv\n|")
    config_result = read_config_file()
    assert config_result == {"delimiter": "|", "display_type": "csv"}
