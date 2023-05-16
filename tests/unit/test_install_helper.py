"""
This module will test the logic pertaining to the installation of files needed for the program.
"""

from io import StringIO
from os import path
from unittest import TestCase
from unittest.mock import patch

from tests.unit.test_helpers import remove_test_files

from todo_cli.config.config_controller import install_config_file
from todo_cli.helpers.install_helper import install_storage_file
from todo_cli.helpers.os_helper import get_config_directory


class TestInstallHelper(TestCase):
    """
    This class will test the logic pertaining to the installation of files needed for the program.
    """

    def __init__(self, method_name: str = ...) -> None:
        self.tasks_directory = f"{get_config_directory()}/tasks.json"
        super().__init__(method_name)

    @patch("sys.stdin", StringIO("tests/unit/\n"))
    def test_install_storage_file(self):
        """
        Tests that the install storage file function works as expected.
        """
        installed_config_file = install_config_file()
        install_storage_file()

        assert installed_config_file is True
        assert path.exists(self.tasks_directory) is True

        with open(self.tasks_directory, "r", encoding="UTF-8") as file:
            assert file.read() == "[]"

        remove_test_files()
