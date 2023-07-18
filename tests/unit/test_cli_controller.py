"""
This module will contain the tests for the cli_controller module
"""
from json import load, dump
from os import path
from tabulate import tabulate

import pytest
from typer.testing import CliRunner


from tests.test_helpers import (
    clean_up,
    STORAGEDIR,
    setup_test_directory,
    setup_test_config,
    setup_test_tasks
)
from todo_cli.cli.cli_controller import app


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


def test_view_command():
    """
    This will test the create command
    """
    tasks_file = path.join(STORAGEDIR, "tasks.json")

    with open(tasks_file, "w", encoding="utf-8") as file:
        dump([{"UUID": "abcd1234", "name": "laundry",
             "date": "2023", "priority": "Low"}], file)

    result = runner.invoke(app, ["view"])
    assert result.exit_code == 0

    expected_table = tabulate(
        [
            ["abcd1234","laundry", "2023", "Low"]
        ],
        headers=["UUID", "name", "date", "priority"],
        tablefmt="rounded_grid"
    )
    assert result.stdout == (expected_table + "\n")


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
