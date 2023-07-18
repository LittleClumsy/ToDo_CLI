"""
This module contains tests for the tasks_helper module.
"""

from unittest import TestCase

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

    def test_create_task(self):
        """
        This function is responsible for testing the create_task function.
        """
        result = create_task(
            task_uuid="abcd1234",
            name="laundry",
            date="2023",
            priority="Low"
        )
        assert result == {
            "UUID": "abcd1234",
            "name": "laundry",
            "date": "2023",
            "priority": "Low"
        }

    def test_install_tasks_file_again(self):
        """
        This function is responsible for testing the install_tasks_file function.
        """
        result = install_tasks_file()
        assert result is False
