"""
This module/file is the entry point for the todo application.
"""
# Built-in imports
import sys

# File imports
from todo_cli.cli.cli_controller import handle_cli_args
from todo_cli.config.config_controller import install_config_file
from todo_cli.helpers.storage_helper import create_storage_directory
from todo_cli.helpers.tasks_helper import install_tasks_file
from todo_cli.logs.logger import create_log


def main(args: list[str]) -> int:
    """
    The entry point for the todo application.

    Args:
        args (list[str]): The CLI arguments. 

    Returns:
        int: The exit code of the application.
    """
    try:
        install_app()
    except FileNotFoundError:
        return handle_install_error()

    create_log("Setting default exit code to 0")
    exit_code = 0

    create_log(f"Handling CLI arguments: {args}")
    handle_cli_args(args)

    create_log(f"Returning exit code: {exit_code}")
    return exit_code


def install_app() -> None:
    """
    Installs the todo application.

    Raises:
        FileNotFoundError: If the application cannot create the storage
            directory or files.
    """
    installed_storage_directory = create_storage_directory()
    installed_config_file = install_config_file()
    install_tasks_file()

    create_log("Starting application")
    create_log(
        f"Installed storage directory: {installed_storage_directory}")
    create_log(f"Installed config file: {installed_config_file}")


def handle_install_error() -> int:
    """
    Handles an install error. This function is called when the application
    cannot create the storage directory or files.

    Returns:
        int: The exit code of the application.

    Examples:
        >>> handle_install_error()
        Install Error [1]: Could not create storage directory or files.
        Please report this issue to the developer.
        [returns] 1
    """
    print("Install Error [1]: Could not create storage directory or files.")
    print("Please report this issue to the developer.")
    return 1


if __name__ == "__main__":
    del sys.argv[0]
    EXIT_CODE = main(sys.argv)
    sys.exit(EXIT_CODE)
