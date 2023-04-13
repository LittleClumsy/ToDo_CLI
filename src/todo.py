"""
This module/file is the entry point for the todo application.
"""
from sys import argv
from config.config_controller import install_config_file, read_config_file
from helpers.install_helper import install_storage_file
from cli.cli_controller import handle_cli_args


def main(args: list[str]):
    """
    The entry point for the todo application.

    Args:
        args (list[str]): The CLI arguments. 
    """
    try:
        config = read_config_file()
    except FileNotFoundError:
        install_config_file()
        config = read_config_file()

    if config["data_storage"] == "":
        install_storage_file()
        config = read_config_file()

    if config["data_storage"] != "":
        handle_cli_args(args)


if __name__ == "__main__":
    del argv[0]
    main(argv)
