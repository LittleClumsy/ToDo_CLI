"""
This module contains unit tests for the os_helper module.
"""
from os import path, removedirs

from todo_cli.helpers.os_helper import (
    get_home_directory,
    get_config_directory,
    create_directory,
    join_paths,
    path_exists
)


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


def test_join_paths():
    """
    Tests the join_paths function
    """
    dir_one = "src"
    dir_two = "tests"
    expected = f"{dir_one}/{dir_two}"
    actual = join_paths(dir_one, dir_two)
    assert expected == actual


def test_path_exists():
    """
    Tests path_exists function
    """
    directory = "tests/unit/test_os_helper.py"

    actual = path_exists(directory)
    assert actual is True
