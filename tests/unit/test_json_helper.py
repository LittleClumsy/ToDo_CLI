"""
This module contains tests for the json_helper module.
"""

import pytest

from todo_cli.helpers.json_helper import (
    read_json_file,
    write_json_file
)


def test_read_json_file():
    """
    This function is responsible for testing the read_json_file function.
    """
    result = read_json_file("tests/data/test.json")
    assert result == {"test": "test"}


def test_read_json_file_that_does_not_exist():
    """
    This function is responsible for testing the read_json_file function when
    the file does not exist.
    """
    with pytest.raises(FileNotFoundError):
        read_json_file("tests/data/does_not_exist.json")


def test_read_invalid_json_file():
    """
    This function is responsible for testing the read_json_file function when
    the file is not a valid json file.
    """
    with pytest.raises(ValueError):
        read_json_file("tests/data/invalid.json")


def test_write_json_file():
    """
    This function is responsible for testing the write_json_file function.
    """
    json_path = "tests/data/writing.json"
    write_json_file(json_path, {"test": "test"})
    result = read_json_file(json_path)
    assert result == {"test": "test"}

    write_json_file(json_path, {})
    result = read_json_file(json_path)
    assert result == {}
