"""
This module will test tasks_helper.
"""
# Global imports
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from helpers.tasks_helper import create_task, view_tasks
from testing.unit.test_helpers import create_test_config, create_test_tasks, remove_test_files



class TestTasksHelper(TestCase):
    """
    This class will test tasks_helper.
    """
    @patch("sys.stdin", StringIO("Laundry\n2023\n"))
    def test_create_task(self):
        """
        Tests create task.
        """
        expected = {
            "name": "Laundry",
            "date": "2023"
        }

        task = create_task()
        assert expected == task

    def test_view_tasks(self):
        """
        This will test view task.
        """
        expected = "Laundry | 2023\nwash | 2023\n"
        create_test_config()
        create_test_tasks()
        with patch("sys.stdout", new=StringIO()) as fake_stdout:
            view_tasks()
            assert fake_stdout.getvalue() == expected 
        remove_test_files()