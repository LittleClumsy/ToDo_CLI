"""
This module will contain all logic pertaining to the configuration of the application.
"""

from helpers.json_helper import write_json_file
from helpers.os_helper import create_directory, get_config_directory

def install_config_file():
    """
    This will install the config file for the application.
    """
    config_directory = get_config_directory()
    create_directory(config_directory)
    write_json_file(f"{config_directory}/config.json", {"data_storage": ""})
