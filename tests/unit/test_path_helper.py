"""
This module contains tests for the path_helper module.
"""

from shutil import rmtree

from todo_cli.helpers.path_helper import (
    create_directory,
    join_paths,
    path_exists
)

TESTDIR = "tests/testing"


def test_create_directory():
    """
    This function is responsible for testing the create_directory function.
    When it is called on a directory that does not exist it should return True.
    """
    result = create_directory(TESTDIR)
    assert result is True
    rmtree(TESTDIR)


def test_double_create_directory():
    """
    This function is responsible for testing the create_directory function.
    When it is called twice on the same directory it should return False the second time.
    """
    create_directory(TESTDIR)
    result = create_directory(TESTDIR)
    assert result is False
    rmtree(TESTDIR)


def test_join_paths():
    """
    This function is responsible for testing the join_paths function.
    """
    result = join_paths("/home/username", ".todo")
    assert result == "/home/username/.todo"


def test_valid_path_exists():
    """
    This function is responsible for testing the path_exists function.
    This will be tested on a valid directory.
    """
    valid_dir = "tests/"
    result = path_exists(valid_dir)
    assert result is True


def test_invalid_path_exists():
    """
    This function is responsible for testing the path_exists function.
    This will be tested on an invalid directory.
    """
    result = path_exists(TESTDIR)
    assert result is False
