"""
This module contains unit tests for the config module.
"""
from json import load

from pytest import raises

from tests.unit.test_helpers import remove_test_files

from todo_cli.config.config_controller import (
    install_config_file,
    read_config_file,
    write_config_file
)
from todo_cli.helpers.os_helper import get_config_directory


def test_install_config_file():
    """
    Tests that the install config file function works as expected.
    """
    expected = {}
    installed_config_file = install_config_file()

    with open(f"{get_config_directory()}/config.json", "r", encoding="UTF-8") as file:
        actual = load(file)

    assert installed_config_file is True
    assert actual == expected
    remove_test_files()


def test_read_config_file():
    """
    This will test the read config file function.
    """
    expected = {}
    installed_config_file = install_config_file()
    actual = read_config_file()
    assert installed_config_file is True
    assert actual == expected
    remove_test_files()


def test_double_install_config_file():
    """
    This will test that the install config file function works as expected when
    the file already exists.
    """
    installed_config_file = install_config_file()
    installed_config_file_again = install_config_file()
    assert installed_config_file is True
    assert installed_config_file_again is False
    remove_test_files()


def test_read_config_file_not_found():
    """
    This will test that the read config file function works as expected when
    the file does not exist.
    """
    with raises(FileNotFoundError):
        read_config_file()


def test_read_config_file_invalid_json():
    """
    This will test that the read config file function works as expected when
    the file is not valid json.
    """
    installed_config_file = install_config_file()
    with open(f"{get_config_directory()}/config.json", "w", encoding="UTF-8") as file:
        file.write("invalid json")
    with raises(ValueError):
        read_config_file()
    remove_test_files()
    assert installed_config_file is True


def test_write_config_file():
    """
    This will test that the write config file function works as expected.
    """
    expected = {"key": "value"}
    installed_config_file = install_config_file()
    write_config_file(expected)
    actual = read_config_file()
    assert installed_config_file is True
    assert actual == expected
    remove_test_files()


def test_write_config_file_with_no_directory():
    """
    This will test that the write config file function works as expected when
    the directory does not exist.
    """
    expected = {"key": "value"}
    with raises(FileNotFoundError):
        write_config_file(expected)
