"""
This module/file is the entry point for the todo application.
"""
# Built-in imports
import sys

# File imports
from todo_cli.cli.cli_controller import app
from todo_cli.config.config_controller import install_config_file
from todo_cli.err.error import handle_json_error, handle_install_error
from todo_cli.helpers.storage_helper import create_storage_directory
from todo_cli.helpers.tasks_helper import install_tasks_file
from todo_cli.logs.logger import create_log


def main() -> int:
    """
    The entry point for the todo application.

    Args:
        args (list[str]): The CLI arguments. 

    Returns:
        int: The exit code of the application.
    """
    try:
        install_app()
    except FileNotFoundError as error:
        return handle_install_error(error)
    except TypeError as error:
        return handle_json_error(error)

    create_log("Setting default exit code to 0")
    exit_code = 0

    create_log("Running Typer app")
    app()

    create_log(f"Returning exit code: {exit_code}")
    return exit_code


def install_app() -> None:
    """
    Installs the todo application.

    Raises:
        FileNotFoundError: If the application cannot create the storage
            directory or files.
        TypeError: If you you try to write a value to a JSON file that is not of
            type dictionary or list.
    """
    installed_storage_directory = create_storage_directory()
    installed_config_file = install_config_file()
    installed_tasks_file = install_tasks_file()

    create_log("Starting application")
    create_log(
        f"Installed storage directory: {installed_storage_directory}")
    create_log(f"Installed config file: {installed_config_file}")
    create_log(f"Installed tasks file: {installed_tasks_file}")


if __name__ == "__main__":
    EXIT_CODE = main()
    sys.exit(EXIT_CODE)
