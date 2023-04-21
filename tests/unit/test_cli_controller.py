"""
This module contains unit tests for the cli controller.
"""
# Global imports
from io import StringIO
from json import dump, load
from os import remove, makedirs, path, rmdir
from unittest import TestCase
from unittest.mock import patch

# File imports
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

    @patch("sys.stdin", StringIO("Laundry\n2023\n"))
    def test_create(self):
        """
        This will test the create command.
        """
        expected = [{
            "name": "Laundry",
            "date": "2023"
        }]

        config_directory = get_config_directory()

        if not path.exists(config_directory):
            makedirs(config_directory)

        tasks_directory = "tests/unit"

        with open(f"{config_directory}/config.json", "w", encoding="UTF-8") as file:
            config = {
                "data_storage": tasks_directory
            }
            dump(config, file)

        with open(f"{tasks_directory}/tasks.json", "w", encoding="UTF-8") as file:
            tasks = []
            dump(tasks, file)

        handle_cli_args(["create"])

        with open(f"{tasks_directory}/tasks.json", "r", encoding="UTF-8") as file:
            tasks = load(file)
            assert expected == tasks

        remove(f"{config_directory}/config.json")
        remove(f"{tasks_directory}/tasks.json")
        rmdir(config_directory)
