"""
This module/file is the entry point for the todo application.
"""
# Built-in imports
import sys

# File imports
from todo_cli.cli.cli_controller import handle_cli_args
from todo_cli.config.config_controller import install_config_file
from todo_cli.helpers.install_helper import install_storage_file
from todo_cli.logs.logger import create_log

def main(args: list[str]) -> int:
    """
    The entry point for the todo application.

    Args:
        args (list[str]): The CLI arguments. 

    Returns:
        int: The exit code of the application.
    """
    install_config_file()
    install_storage_file()
    create_log("Starting application")
    create_log("Installed required files")

    create_log("Setting default exit code to 0")
    exit_code = 0

    create_log(f"Handling CLI arguments: {args}")
    handle_cli_args(args)

    create_log(f"Returning exit code: {exit_code}")
    return exit_code


if __name__ == "__main__":
    del sys.argv[0]
    EXIT_CODE = main(sys.argv)
    sys.exit(EXIT_CODE)
