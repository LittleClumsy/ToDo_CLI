"""
This module will test the logger module.
"""
from todo_cli.config.config_controller import get_config_directory
from todo_cli.logs.logger import create_log
from tests.unit.test_helpers import remove_test_files, create_test_files

def test_create_log():
    """
    This will test the create log function.
    """
    create_test_files()
    create_log("HELLO")
    config_directory = get_config_directory()
    with open(f"{config_directory}/logs.txt", "r", encoding="UTF-8") as file:
        lines = file.readlines()
        assert lines[0].endswith("HELLO\n") is True
    remove_test_files()
