"""This module will contain helper functions for tests."""

from os import remove
from config.config_controller import write_config_file, install_config_file
from helpers.tasks_helper import write_tasks_file





def create_test_config():
    install_config_file()
    test_config = {"data_storage" : "src/testing/unit"}
    write_config_file(test_config)

def create_test_tasks():
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
    remove("src/testing/unit/tasks.json")
    write_config_file({})
    