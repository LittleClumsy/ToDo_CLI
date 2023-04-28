"""
This module/file is the entry point for the todo application.
"""
# Built-in imports
import sys

# File imports
from todo_cli.cli.cli_controller import handle_cli_args
from todo_cli.config.config_controller import (
    install_config_file,
    get_config_directory,
    read_config_file,
    install_config_directory
)
from todo_cli.helpers.install_helper import install_storage_file
from todo_cli.helpers.os_helper import path_exists
from todo_cli.logs.logger import create_log

def main(args: list[str]) -> int:
    """
    The entry point for the todo application.

    Args:
        args (list[str]): The CLI arguments. 

    Returns:
        int: The exit code of the application.
    """
    install_config_directory()
    create_log("Started program")

    # Default exit code (0 = no errors)
    exit_code = 0

    # Check if the config file exists
    config_directory = get_config_directory()
    config_exists = path_exists(f"{config_directory}/config.json")
    create_log(f"Config directory: {config_directory}")
    create_log(f"Config exists: {config_exists}")

    # Check if the config file is valid
    config_is_valid = False
    if config_exists:
        config = read_config_file()
        config_is_valid = path_exists(config["data_storage"])
    create_log(f"Config is valid: {config_is_valid}")

    # If the config file doesn't exist or is not valid, install program files
    if not config_exists or not config_is_valid:
        create_log("Installing program files")
        install_config_file()
        install_storage_file()
        create_log("Installed program files")

    create_log(f"Ran program with arguments: {args}")
    handle_cli_args(args)

    create_log(f"Exited with exit code: {exit_code}")
    return exit_code


if __name__ == "__main__":
    del sys.argv[0]
    EXIT_CODE = main(sys.argv)
    sys.exit(EXIT_CODE)
