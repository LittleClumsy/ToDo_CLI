"""
This module/file is the entry point for the todo application.
"""

# Built-in imports
import sys

# File imports
from cli.cli_controller import handle_cli_args
from config.config_controller import install_config_file, get_config_directory
from helpers.install_helper import install_storage_file
from helpers.os_helper import path_exists


def main(args: list[str]) -> int:
    """
    The entry point for the todo application.

    Args:
        args (list[str]): The CLI arguments. 

    Returns:
        int: The exit code of the application.
    """
    # Default exit code (0 = no errors)
    exit_code = 0

    # Check if the config file exists
    config_directory = get_config_directory()
    config_exists = path_exists(f"{config_directory}/config.json")

    # If the config file doesn't exist, install program files
    if not config_exists:
        install_config_file()
        install_storage_file()

    handle_cli_args(args)

    return exit_code


if __name__ == "__main__":
    del sys.argv[0]
    EXIT_CODE = main(sys.argv)
    sys.exit(EXIT_CODE)
