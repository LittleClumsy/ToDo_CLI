"""
This module contains tests for the tasks_helper module.
"""

from io import StringIO

from unittest import TestCase
from unittest.mock import patch

import pytest

from tests.test_helpers import (
    setup_test_directory,
    clean_up
)

from todo_cli.helpers.tasks_helper import (
    install_tasks_file,
    read_tasks_file,
    write_tasks_file,
    create_task,
    view_tasks
)


class TestTasksHelper(TestCase):
    """
    This class contains the tests for the tasks_helper module.
    """
    @pytest.fixture(autouse=True)
    def run_before_and_after_tests(self):
        """
        This function will run the clean_up function before and after the tests.
        """
        setup_test_directory()
        install_tasks_file()
        yield
        clean_up()

    def test_read_tasks_file(self):
        """
        This function is responsible for testing the read_tasks_file function.
        """
        result = read_tasks_file()
        assert result == []

    def test_read_tasks_file_when_it_does_not_exist(self):
        """
        This function is responsible for testing the read_tasks_file function.
        """
        clean_up()
        with pytest.raises(FileNotFoundError):
            read_tasks_file()

    def test_write_tasks_file(self):
        """
        This function is responsible for testing the write_tasks_file function.
        """
        write_tasks_file([{"test": "test"}])
        result = read_tasks_file()
        assert result == [{"test": "test"}]

    @patch("sys.stdin", StringIO("laundry\n2023\n"))
    def test_create_task(self):
        """
        This function is responsible for testing the create_task function.
        """
        result = create_task()
        assert result == {"name": "laundry", "date": "2023"}

    def test_view_tasks(self):
        """
        This function is responsible for testing the view_tasks function.
        """
        write_tasks_file(
            [
                {
                    "name": "laundry",
                    "date": "2023"
                },
                {
                    "name": "dishes",
                    "date": "2022"
                }
            ]
        )
        with patch("sys.stdout", new=StringIO()) as fake_out:
            view_tasks()
            assert fake_out.getvalue() == "laundry | 2023\ndishes | 2022\n"
