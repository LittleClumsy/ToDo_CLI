"""
This module will contain the tests for the cli_controller module
"""
from json import load, dump
from os import path

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
    result = runner.invoke(app, ["create"], input="laundry\n2023\n")
    assert result.exit_code == 0

    tasks_file = path.join(STORAGEDIR, "tasks.json")
    file_result = []
    with open(tasks_file, "r", encoding="utf-8") as file:
        file_result = load(file)
    assert file_result[0].get("UUID") is not None
    assert file_result[0].get("name") == "laundry"
    assert file_result[0].get("date") == "2023"


def test_view_command():
    """
    This will test the create command
    """
    tasks_file = path.join(STORAGEDIR, "tasks.json")

    with open(tasks_file, "w", encoding="utf-8") as file:
        dump([{"UUID": "abcd1234", "name": "laundry", "date": "2023"}], file)

    result = runner.invoke(app, ["view"])
    assert result.exit_code == 0
    assert result.stdout == "abcd1234 | laundry | 2023\n"


def test_edit_command():
    """
    This will test the edit command
    """
    tasks_file = path.join(STORAGEDIR, "tasks.json")

    with open(tasks_file, "w", encoding="utf-8") as file:
        dump([{"UUID": "abcd1234", "name": "laundry", "date": "2018"}], file)

    result = runner.invoke(app, ["edit"], input="abcd1234\ndate\n2023\n")
    assert result.exit_code == 0

    file_result = []
    with open(tasks_file, "r", encoding="utf-8") as file:
        file_result = load(file)
    assert file_result == [
        {"UUID": "abcd1234", "name": "laundry", "date": "2023"}]


def test_edit_command_with_uuid():
    """
    This will test that edit command fails if you try edit uuid field.
    """
    result = runner.invoke(
        app, ["edit", "--task-id", "abcd1234", "--field-name", "UUID", "--value", "2023"])
    assert result.exit_code == 3
    assert result.stdout == "Invalid field. The UUID can not be edited.\n"


def test_edit_command_with_invalid_field():
    """
    This will test that edit command fails if you try edit uuid field.
    """
    result = runner.invoke(
        app, ["edit", "--task-id", "abcd1234", "--field-name", "eggs", "--value", "2023"])
    assert result.exit_code == 3
    assert result.stdout == "That field does not exist! Please select a valid field to edit.\n"
