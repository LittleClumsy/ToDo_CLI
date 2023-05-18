"""
This module will contain the tests for the config_controller module.
"""

import pytest

from tests.test_helpers import clean_up, setup_test_directory, setup_test_config

from todo_cli.config.config_controller import (
    get_config_path,
    install_config_file,
    read_config_file,
    write_config_file
)


@pytest.fixture(autouse=True)
def run_before_and_after_tests():
    """
    This function will run the clean_up function before and after the tests.
    """
    yield
    clean_up()


def test_get_config_path():
    """
    This function is responsible for testing the get_config_path function.
    """
    result = get_config_path()
    assert result.endswith(".todo/config.json") is True


def test_install_config_file():
    """
    This function is responsible for testing the install_config_file function.
    """
    setup_test_directory()
    result = install_config_file()
    assert result is True


def test_double_install_config_file():
    """
    This function is responsible for testing the install_config_file function.
    This will be tested when the config file already exists. It should return False.
    """
    setup_test_directory()
    install_config_file()
    result = install_config_file()
    assert result is False


def test_install_config_file_with_no_dir():
    """
    This function is responsible for testing the install_config_file function.
    """
    with pytest.raises(FileNotFoundError):
        install_config_file()


def test_read_config_file():
    """
    This function is responsible for testing the read_config_file function.
    """
    setup_test_directory()
    setup_test_config()
    result = read_config_file()
    assert result == {"test": "Config"}


def test_read_config_file_with_no_dir():
    """
    This function is responsible for testing the read_config_file function.
    """
    with pytest.raises(FileNotFoundError):
        read_config_file()


def test_read_config_file_with_invalid_json():
    """
    This function is responsible for testing the read_config_file function.
    """
    setup_test_directory()
    setup_test_config("INVALID JSON")
    with pytest.raises(ValueError):
        read_config_file()


def test_write_config_file():
    """
    This function is responsible for testing the write_config_file function.
    """
    setup_test_directory()
    write_config_file({"testing": "Config"})
    result = read_config_file()
    assert result == {"testing": "Config"}


def test_write_config_file_no_dir():
    """
    This function is responsible for testing the write_config_file function.
    """
    with pytest.raises(FileNotFoundError):
        write_config_file({"testing": "Config"})
