from setuptools import setup, find_packages

version = open("version.txt").read().strip()


def read_requirements() -> list[str]:
    """Read the requirements from the requirements.txt file."""
    lines = []
    with open("requirements.txt") as req:
        lines = req.readlines()
        lines.pop(0)
    return [line.strip() for line in lines]


exclude_files = ["tests/*"]

setup(
    name="todo",
    version=version,
    author="Brendon & Evan",
    author_email="Bengelbrecht2002@gmail.com",
    description="A basic Todo CLI program",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LittleClumsy/ToDo_CLI",
    packages=find_packages(
        where=".",
        exclude=exclude_files,
    ),
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "todo = todo:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    include_package_data=True,
)
