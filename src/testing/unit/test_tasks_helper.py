"""
This module will test tasks_helper.
"""
# Global imports
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from helpers.tasks_helper import create_task


class TestCliController(TestCase):
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
