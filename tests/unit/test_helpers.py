"""This module will contain helper functions for tests."""

from os import remove
from todo_cli.config.config_controller import write_config_file, install_config_file
from todo_cli.helpers.tasks_helper import write_tasks_file

def create_test_config():
    """
    This function will create a test config file.
    """
    install_config_file()
    test_config = {"data_storage" : "tests/unit"}
    write_config_file(test_config)

def create_test_tasks():
    """
    This function will create a test tasks file.
    """
    test_tasks = [
        {
            "name": "Laundry",
            "date": "2023"
        },
        {
            "name": "wash",
            "date": "2023"
        }
    ]
    write_tasks_file(test_tasks)

def remove_test_files():
    """
    This function will remove the test files.
    """
    remove("tests/unit/tasks.json")
    write_config_file({})
