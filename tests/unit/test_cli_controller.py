"""
This module contains unit tests for the cli controller.
"""
# Global imports
from io import StringIO
from json import load
from unittest import TestCase
from unittest.mock import patch

# File imports
from tests.unit.test_helpers import (
    create_test_config,
    create_test_tasks,
    remove_test_files,
    create_test_files
)

from todo_cli.cli.cli_controller import handle_cli_args
from todo_cli.helpers.os_helper import get_config_directory

class TestCliController(TestCase):
    """
    This class contains unit test for the CLI Controller.
    """

    def test_handle_cli_args_with_no_args(self):
        """
        This will test handle_cli_args without arguments
        """
        with patch("sys.stdout", new=StringIO()) as fake_stdout:
            handle_cli_args([])
            assert fake_stdout.getvalue() == "This should be the help command.\n"

    @patch("sys.stdin", StringIO("Fishing\n2020\n"))
    def test_create(self):
        """
        This will test the create command.
        """
        create_test_files()
        config_directory = get_config_directory()
        expected = [
            {
                "name": "Laundry",
                "date": "2023"
            },
            {
                "name": "wash",
                "date": "2023"
            },
            {
                "name": "Fishing",
                "date": "2020"
            }
        ]

        handle_cli_args(["create"])

        with open(f"{config_directory}/tasks.json", "r", encoding="UTF-8") as file:
            tasks = load(file)
            assert expected == tasks
        remove_test_files()

    def test_view_tasks(self):
        """
        This will test view task.
        """
        expected = "Laundry | 2023\nwash | 2023\n"
        create_test_config()
        create_test_tasks()
        with patch("sys.stdout", new=StringIO()) as fake_stdout:
            handle_cli_args(["view"])
            assert fake_stdout.getvalue() == expected
        remove_test_files()
