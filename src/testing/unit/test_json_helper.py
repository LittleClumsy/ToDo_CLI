"""
This module contains unit tests for the json_helper module.
"""

from os import path, remove

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
