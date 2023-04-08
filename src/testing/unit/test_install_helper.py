"""
This module will test the logic pertaining to the installation of files needed for the program.
"""

from io import StringIO
from os import path, remove
from unittest import TestCase
from unittest.mock import patch

from helpers.install_helper import install_storage_file


class TestInstallHelper(TestCase):
    """
    This class will test the logic pertaining to the installation of files needed for the program.
    """
    
    
    def __init__(self, methodName: str = ...) -> None:
        self.VALID_TASK_PATH = "src/testing/unit/tasks.json"
        super().__init__(methodName)
        

    @patch("sys.stdin", StringIO("src/testing/unit/\n"))
    def test_install_storage_file(self):
        """
        Tests that the install storage file function works as expected.
        """
        install_storage_file()
        assert path.exists(self.VALID_TASK_PATH) is True

        with open(self.VALID_TASK_PATH, "r", encoding="UTF-8") as file:
            assert file.read() == "[]"

        remove(self.VALID_TASK_PATH)

    @patch("sys.stdin", StringIO("src/unit/\n"))
    def test_install_storage_file_invalid_path(self):
        """
        Tests that the install storage file function displays the correct error message.
        """
        with patch("sys.stdout", new=StringIO()) as fake_stdout:
            install_storage_file()
            assert fake_stdout.getvalue() == "Enter the directory path where you" + \
                " want to install the file: This path doesn't exist.\n"
        assert path.exists("src/unit/tasks.json") is False

    @patch("sys.stdin", StringIO("src/testing/unit/\n"))
    def test_install_storage_file_already_existing_file(self):
        """
        Tests that the install storage file function displays the correct error message.
        """
        with open(self.VALID_TASK_PATH, "w", encoding="UTF-8") as file:
            file.write("// This is a test file.")

        with patch("sys.stdout", new=StringIO()) as fake_stdout:
            install_storage_file()
            assert fake_stdout.getvalue() == "Enter the directory path where you" + \
                " want to install the file: This file already exists in this directory.\n"

        assert path.exists(self.VALID_TASK_PATH) is True

        remove(self.VALID_TASK_PATH)
