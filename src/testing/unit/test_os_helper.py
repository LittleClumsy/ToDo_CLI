"""
This module contains unit tests for the os_helper module.
"""
from os import path, removedirs

from helpers.os_helper import get_home_directory, get_config_directory, create_directory

def test_get_home_directory():
    """
    Tests the get_home_directory function.
    """
    expected = path.expanduser("~")
    actual = get_home_directory()
    assert expected == actual

def test_get_config_directory():
    """
    Tests the get_config_directory function.
    """
    expected = f"{get_home_directory()}/.todo"
    actual = get_config_directory()
    assert expected == actual

def test_create_directory():
    """
    Tests the create_directory function.
    """
    folder_path = "temp/test/"
    create_directory(folder_path)
    assert path.exists(folder_path)
    create_directory(folder_path)
    removedirs(folder_path)
