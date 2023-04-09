"""
This module contains unit tests for the json_helper module.
"""
# Global imports
from os import path, remove

# Third party imports
from pytest import raises

# Local imports
from helpers.json_helper import read_json_file
from helpers.json_helper import write_json_file


def test_write_json_file():
    """
    Tests the write_json_file function.
    """
    expected = '{\n    "test": "Hi",\n    "age": 30\n}'

    file_path = "test.json"
    content = {"test": "Hi", "age": 30}
    write_json_file(file_path, content)

    with open(file_path, "r", encoding="UTF-8") as file:
        actual = file.read()

    assert path.exists(file_path)
    assert expected == actual

    remove(file_path)


def test_read_json_file():
    """
    Tests the read_json_file function.
    """
    file_path = "src/testing/test.json"
    mock_content = '{\n    "test": "Hi",\n    "age": 30\n}'
    expected = {'test': 'Hi', 'age': 30}

    with open(file_path, "w", encoding="UTF-8") as file:
        file.write(mock_content)

    actual = read_json_file(file_path)

    assert path.exists(file_path)
    assert expected == actual

    remove(file_path)


def test_read_json_when_file_does_not_exist():
    """
    Tests the read_json_file function when the file does not exist.
    """
    file_path = "src/testing/test.json"
    with raises(FileNotFoundError):
        read_json_file(file_path)


def test_read_json_when_invalid_content():
    """
    Tests the read_json_file function when the file does not contain valid json.
    """
    file_path = "src/testing/test.json"
    mock_content = 'asdfghhjkl'

    with open(file_path, "w", encoding="UTF-8") as file:
        file.write(mock_content)

    with raises(ValueError):
        read_json_file(file_path)

    remove(file_path)
