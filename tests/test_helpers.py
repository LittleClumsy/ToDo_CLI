"""
This module contains helper functions for the tests.
"""

from os import path, makedirs
from shutil import rmtree

STORAGEDIR = path.join(path.expanduser("~"), ".todo")


def setup_test_directory():
    """
    This function is responsible for setting up the test directory.
    """
    if not path.exists(STORAGEDIR):
        makedirs(STORAGEDIR)


def setup_test_config(content="{\"test\": \"Config\"}"):
    """
    This function is responsible for setting up the test config.
    """
    config_file = path.join(STORAGEDIR, "config.json")
    with open(config_file, "w", encoding="utf-8") as file:
        file.write(content)


def clean_up():
    """
    This function is responsible for cleaning up the storage directory.
    """
    if path.exists(STORAGEDIR):
        rmtree(STORAGEDIR)
