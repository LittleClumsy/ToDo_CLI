"""
This will test the error module.
"""

from todo_cli.err.error import (
    handle_install_error,
    handle_json_error
)


def test_handle_install_error():
    """
    This function is responsible for testing the handle_install_error function.
    """
    error = Exception("This should be an install error")
    result = handle_install_error(error)
    assert result == 1


def test_handle_json_error():
    """
    This function is responsible for testing the handle_json_error function.
    """
    error = Exception("This should be a json error")
    result = handle_json_error(error)
    assert result == 2
