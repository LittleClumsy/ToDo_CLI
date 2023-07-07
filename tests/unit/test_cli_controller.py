"""
This module will contain the tests for the cli_controller module
"""
from json import load
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
    assert file_result == [{"name": "laundry", "date": "2023"}]


def test_view_command():
    """
    This will test the create command
    """
    runner.invoke(app, ["create"], input="laundry\n2023\n")
    result = runner.invoke(app, ["view"])
    assert result.exit_code == 0
    assert result.stdout == "laundry | 2023\n"
