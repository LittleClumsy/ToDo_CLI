"""
This module will test the todo.py module
"""
from os import remove

from config.config_controller import install_config_file
from helpers.os_helper import get_config_directory
from todo import main


def test_main_returns_0():
    """
    This function will test that the main function returns 0
    """
    install_config_file()
    assert main([]) == 0
