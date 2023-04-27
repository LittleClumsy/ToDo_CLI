"""
This module contains unit tests for the config module.
"""
from json import load
from os import remove, removedirs

from todo_cli.config.config_controller import install_config_file
from todo_cli.helpers.os_helper import get_config_directory


def test_install_config_file():
    """
    Tests that the install config file function works as expected.
    """
    install_config_file()
    with open(f"{get_config_directory()}/config.json", "r", encoding="UTF-8") as file:
        actual = load(file)
    expected = {"data_storage": ""}
    assert actual == expected
    remove(f"{get_config_directory()}/config.json")
    removedirs(get_config_directory())