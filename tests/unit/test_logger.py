"""
This module contains tests for the logger module.
"""

from os import path

from tests.test_helpers import (
    setup_test_directory,
    clean_up
)

from todo_cli.logs.logger import create_log


def test_create_log():
    """
    This function is responsible for testing the create_log function.
    """
    home_directory = path.expanduser("~")
    storage_directory = path.join(home_directory, ".todo")
    log_directory = path.join(storage_directory, "logs.txt")

    setup_test_directory()
    create_log("test")
    with open(log_directory, "r", encoding="UTF-8") as log_file:
        log_file_contents = log_file.readlines()
        assert log_file_contents[-1].endswith("test\n") is True

    clean_up()
