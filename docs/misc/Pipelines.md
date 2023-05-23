# Pipelines docs

## Table of Contents

* [Ubuntu Pipelines](#ubuntu_pipelines)
* [Setup](#setup)
* [Testing](#testing)
* [Lint](#lint)
* [Build](#build)

## Ubuntu_Pipelines

This is a way to automatically test if our program will build successfully.

### Setup

This step will ensure that the latest version of pip is installed.

```bash
pip install --upgrade pip
```

Pipenv will be installed.

```bash
pip install pipenv
```

Lastly pipenv will be used to install all the dev packages from Pipfile.

```bash
pipenv install --dev
```

### Testing

This will run all of our tests that reside in the tests folder. 

```bash
pipenv run pytest -q tests/
```

### Lint

We use pylint to ensure consistency and readability of our code.  
This will check our code in the folder todo_cli.

```bash
pipenv run pylint todo_cli/
```

This will print to the terminal to indicate the start of linting tests.

```bash
echo "Linting Tests..."
```

We then Lint our tests in the tests/ folder.

```bash
pipenv run pylint tests/
```

### Build

We use PyInstaller to create a single .exe file for our program. This will test that there are no problems when building it.

```bash
pipenv run pyinstaller --onefile todo.py
```










