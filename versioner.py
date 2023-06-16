"""This file is used to keep track of the version of the program"""
from os import getenv
from sys import argv
from dotenv import load_dotenv


def main(args: list[str]):
    """
    This function is the main function of the program, it will take the arguments and
    run the program accordingly.
    """
    load_dotenv(".env")
    version = getenv("VERSION")
    version = version.split(".")

    if len(args) != 2:
        print("Invalid Arguments")
        exit(1)
    elif args[1] == "patch":
        version[2] = str(int(version[2]) + 1)
    elif args[1] == "minor":
        version[1] = str(int(version[1]) + 1)
        version[2] = "0"
    elif args[1] == "major":
        version[0] = str(int(version[0]) + 1)
        version[1] = "0"
        version[2] = "0"

    version = ".".join(version)

    with open(".env", "r", encoding="utf-8") as file:
        lines = file.readlines()

    for index, line in enumerate(lines):
        if line.startswith("VERSION"):
            lines[index] = f"VERSION={version}\n"

    with open(".env", "w", encoding="utf-8") as file:
        file.writelines(lines)

if __name__ == "__main__":
    main(argv)
