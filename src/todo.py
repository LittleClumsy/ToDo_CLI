"""
This module/file is the entry point for the todo application.
"""

from config.config_controller import install_config_file
from helpers.install_helper import install_storage_file

def main():
    """
    The entry point for the todo application.
    """
    install_config_file()
    install_storage_file()


if __name__ == "__main__":
    main()
