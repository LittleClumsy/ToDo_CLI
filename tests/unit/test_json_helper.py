"""
This module contains unit tests for the json_helper module.
"""
# Global imports
from os import path, remove

# Third party imports
from pytest import raises

# Local imports
from todo_cli.helpers.json_helper import read_json_file
from todo_cli.helpers.json_helper import write_json_file

FILE_PATH = "tests/test.json"


def test_write_json_file():
    """
    Tests the write_json_file function.
    """
    expected = '{\n    "test": "Hi",\n    "age": 30\n}'

    content = {"test": "Hi", "age": 30}
    write_json_file(FILE_PATH, content)

    with open(FILE_PATH, "r", encoding="UTF-8") as file:
        actual = file.read()

    assert path.exists(FILE_PATH)
    assert expected == actual

    remove(FILE_PATH)


def test_read_json_file():
    """
    Tests the read_json_file function.
    """
    mock_content = '{\n    "test": "Hi",\n    "age": 30\n}'
    expected = {'test': 'Hi', 'age': 30}

    with open(FILE_PATH, "w", encoding="UTF-8") as file:
        file.write(mock_content)

    actual = read_json_file(FILE_PATH)

    assert path.exists(FILE_PATH)
    assert expected == actual

    remove(FILE_PATH)


def test_read_json_when_file_does_not_exist():
    """
    Tests the read_json_file function when the file does not exist.
    """
    with raises(FileNotFoundError):
        read_json_file(FILE_PATH)


def test_read_json_when_invalid_content():
    """
    Tests the read_json_file function when the file does not contain valid json.
    """
    mock_content = 'asdfghhjkl'

    with open(FILE_PATH, "w", encoding="UTF-8") as file:
        file.write(mock_content)

    with raises(ValueError):
        read_json_file(FILE_PATH)

    remove(FILE_PATH)
