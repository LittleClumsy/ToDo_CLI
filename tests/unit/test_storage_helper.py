"""
This module is responsible for testing the storage_helper module.
"""
import pytest

from tests.test_helpers import clean_up

from todo_cli.helpers.storage_helper import (
    get_storage_directory,
    create_storage_directory
)


@pytest.fixture(autouse=True)
def run_before_and_after_tests():
    """
    This function will run the clean_up function before and after the tests.
    """
    yield
    clean_up()


def test_get_storage_directory():
    """
    This function is responsible for testing the get_storage_directory function.
    """
    result = get_storage_directory()
    assert result.endswith(".todo") is True


def test_create_storage_directory():
    """
    This function is responsible for testing the create_storage_directory function.
    """
    result = create_storage_directory()
    assert result is True


def test_double_create_storage_directory():
    """
    This function is responsible for testing the create_storage_directory function.
    This will be tested when the directory already exists. It should return False.
    """
    create_storage_directory()
    result = create_storage_directory()
    assert result is False
