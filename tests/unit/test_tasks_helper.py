"""
This module contains tests for the tasks_helper module.
"""

from json import load, dump
from os import path
from unittest.mock import patch
from unittest import TestCase
from typer import Exit
from typer.testing import CliRunner

import pytest

from tests.test_helpers import (
    setup_test_directory,
    clean_up,
    STORAGEDIR
)

from todo_cli.helpers.tasks_helper import (
    install_tasks_file,
    read_tasks_file,
    write_tasks_file,
    create_task,
    validate_task_ids,
    delete_task
)
from todo_cli.cli.cli_controller import app

runner = CliRunner()


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

    def test_validate_task_ids(self):
        """
        This function is responsible for testing the install_tasks_file function.
        """
        result = validate_task_ids(['123'], [{"UUID": "2345"}])
        assert result is False

    def test_delete_tasks_if_validation_failed(self):
        """
        This function is responsible for testing the delete_task function.
        """
        write_tasks_file([{"UUID": "2345"}])
        with pytest.raises(Exit):
            delete_task(['123'])
            
    def test_delete_task_valid_id_confirmation_no(self):
        write_tasks_file([{"UUID": "123"}])
        
        with patch("typer.confirm", return_value=False) as mock_confirm, \
            patch("builtins.print") as mock_print:
            
            with pytest.raises(Exit) as e:
                delete_task(['123'])
            
            assert e.value.exit_code == 0
            mock_confirm.assert_called_once()
            mock_print.assert_called_with("Not deleting task.")
            
    def test_delete_task(self):
        """
        This function is responsible for testing the delete task
        """
        result = write_tasks_file([{"UUID": "123"}])
        
        with patch("typer.confirm", return_value=True) as mock_confirm, \
            patch("builtins.print") as mock_print:
            
            delete_task(['123'])
            
            mock_confirm.assert_called_once()
            mock_print.assert_any_call("Deleted task with ID(s): ['123']")
            