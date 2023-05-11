"""
This module contains all logic pertaining to the creation, writing and editing of text file logs.
"""

from datetime import datetime

from todo_cli.config.config_controller import get_config_directory

def create_log(log_details: str):
    """
    This function updates the log file with the string passed in as an argument.
    
    Args:
        log_details (str): The string to be written to the log file.
    """
    config_directory = get_config_directory()
    with open(f"{config_directory}/logs.txt", "a+", encoding="UTF-8") as log_file:
        log_file.write(f"{datetime.now()} - {log_details}\n")
