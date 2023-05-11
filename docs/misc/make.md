# Makefile docs

## Table of Contents

* [Introduction](#introduction)
* [Usage](#usage)
* [Commands](#commands)
* [Variables](#variables)

## Introduction

This document is a guide to the Makefile used in this project.

What is a Makefile? A Makefile is a file containing a set of directives used with the `make` command to build and maintain programs. It is used to simplify the process of running commands and scripts.

Our Makefile is used to version, build, test and more.

## Usage

To use the Makefile, simply run `make` followed by the command you wish to run.
You have to be in the directory where the Makefile is located.

## Commands

### Patch

This command will bump the patch version of the project. This will also update the sonar project version. We keep track of the version in the `VERSION` file.

```bash
make patch
```

### Minor

This command will bump the minor version of the project. This will also update the sonar project version. We keep track of the version in the `VERSION` file.

```bash
make minor
```

### Major

This command will bump the major version of the project. This will also update the sonar project version. We keep track of the version in the `VERSION` file.

```bash
make major
```

### Setup

This command will install all development dependencies. This is useful when you first clone the project. It uses pipenv to install the dependencies.

```bash
make setup
```

### Setup (Build)

This command will install only user dependencies. This is useful when you want to run the project. It uses pipenv to install the dependencies.

```bash
make setup-build
```

### Clean

This command will uninstall all unused dependencies inside the virtual environment. It uses pipenv to uninstall the dependencies.

It will also delete pytest cache files, coverage files and temporary test files.

```bash
make clean
```

### Coverage

This command generates a coverage report. It uses pytest to run the tests and generate the report. It will also open a browser with the report.

```bash
make coverage
```

### Lint

This command will run the linter. It uses pylint to run the linter.

```bash
make lint
```

### Test

This command will run all the tests. It uses pytest to run the tests.

```bash
make test
```

### Unit Test

This command will run the unit tests. It uses pytest to run the tests.

```bash
make unit-test
```

### Update

This command will update the project dependencies. It uses pipenv to update the dependencies. This will update the Pipfile.lock and requirements.txt with info on the updated dependencies.

It will also delete any unused dependencies.

```bash
make update
```

### Pipeline

This command will run the commands that are run as part of the pipeline. It will run the linter and tests.

```bash
make pipeline
```

## Variables

There are variables that are used in the Makefile to make versioning possible.

### PACKAGE_VERSION

This variable is used to store the version of the project that is stored in the `VERSION` file.

### major

This variable is used to store the major version of the project. It is used to keep track of the current version.

### minor

This variable is used to store the minor version of the project. It is used to keep track of the current version.

### patch

This variable is used to store the patch version of the project. It is used to keep track of the current version.

### newMajor

This variable is used to store the new major version of the project. It is used to keep track of the new version.

### newMinor

This variable is used to store the new minor version of the project. It is used to keep track of the new version.

### newPatch

This variable is used to store the new patch version of the project. It is used to keep track of the new version.
