"""
This module contains helper functions for the tests.
"""
import json
from os import path, makedirs
from shutil import rmtree

STORAGEDIR = path.join(path.expanduser("~"), ".todo")


def setup_test_directory():
    """
    This function is responsible for setting up the test directory.
    """
    if not path.exists(STORAGEDIR):
        makedirs(STORAGEDIR)


def setup_test_config(content: dict | list = {"test": "Config"}):
    """
    This function is responsible for setting up the test config.
    """
    config_file = path.join(STORAGEDIR, "config.json")
    with open(config_file, "w", encoding="utf-8") as file:
        json_content = json.dumps(content, indent=4)
        file.write(json_content)


def setup_test_tasks(content="[]"):
    """
    This function is responsible for setting up the test config.
    """
    tasks_file = path.join(STORAGEDIR, "tasks.json")
    with open(tasks_file, "w", encoding="utf-8") as file:
        file.write(content)


def clean_up():
    """
    This function is responsible for cleaning up the storage directory.
    """
    if path.exists(STORAGEDIR):
        rmtree(STORAGEDIR)
