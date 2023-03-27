"""
This module/file is the entry point for the todo application.
"""

from config.config_controller import install_config_file

def main():
    """
    The entry point for the todo application.
    """
    install_config_file()

if __name__ == "__main__":
    main()
