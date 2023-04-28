"""
This module will test the logic pertaining to the installation of files needed for the program.
"""

from io import StringIO
from os import path, remove
from unittest import TestCase
from unittest.mock import patch

from todo_cli.config.config_controller import install_config_file
from todo_cli.helpers.install_helper import install_storage_file
from todo_cli.helpers.os_helper import get_config_directory


class TestInstallHelper(TestCase):
    """
    This class will test the logic pertaining to the installation of files needed for the program.
    """

    def __init__(self, method_name: str = ...) -> None:
        self.valid_task_path = "tests/unit/tasks.json"
        super().__init__(method_name)

    @patch("sys.stdin", StringIO("tests/unit/\n"))
    def test_install_storage_file(self):
        """
        Tests that the install storage file function works as expected.
        """
        install_config_file()
        install_storage_file()
        assert path.exists(self.valid_task_path) is True

        with open(self.valid_task_path, "r", encoding="UTF-8") as file:
            assert file.read() == "[]"

        remove(self.valid_task_path)
        remove(f"{get_config_directory()}/config.json")

    @patch("sys.stdin", StringIO("unit/\ntests/unit/\n"))
    def test_install_storage_file_invalid_path(self):
        """
        Tests that the install storage file function displays the correct error message.
        """
        install_config_file()

        with patch("sys.stdout", new=StringIO()) as fake_stdout:
            install_storage_file()
            assert fake_stdout.getvalue() == "Enter the directory path where you" + \
                " want to install the file: This path doesn't exist.\n" + \
                "Enter the directory path where you want to install the file: "
        assert path.exists("unit/tasks.json") is False

        remove(self.valid_task_path)
        remove(f"{get_config_directory()}/config.json")

    @patch("sys.stdin", StringIO("tests/unit/\ntests/\n"))
    def test_install_storage_file_already_existing_file(self):
        """
        Tests that the install storage file function displays the correct error message.
        """
        install_config_file()

        with open(self.valid_task_path, "w", encoding="UTF-8") as file:
            file.write("// This is a test file.")

        with patch("sys.stdout", new=StringIO()) as fake_stdout:
            install_storage_file()
            assert fake_stdout.getvalue() == "Enter the directory path where you" + \
                " want to install the file: This file already exists in this directory.\n" + \
                "Enter the directory path where you want to install the file: "

        assert path.exists(self.valid_task_path) is True

        remove(self.valid_task_path)
        remove("tests/tasks.json")
        remove(f"{get_config_directory()}/config.json")
