# ToDo_CLI
ToDo_CLI is still very early in development. Currently it's a simple CLI program to help you keep track of all your tasks.

<p align="center">
    <img src="https://sonarcloud.io/api/project_badges/measure?project=LittleClumsy_ToDo_CLI&metric=coverage">
    <img src="https://sonarcloud.io/api/project_badges/measure?project=LittleClumsy_ToDo_CLI&metric=ncloc">
</p>
<p align="center">
    <img src="https://sonarcloud.io/api/project_badges/measure?project=LittleClumsy_ToDo_CLI&metric=reliability_rating">
    <img src="https://sonarcloud.io/api/project_badges/measure?project=LittleClumsy_ToDo_CLI&metric=security_rating">
    <img src="https://sonarcloud.io/api/project_badges/measure?project=LittleClumsy_ToDo_CLI&metric=sqale_rating">
</p>
<p align="center">
    <img src="https://sonarcloud.io/api/project_badges/measure?project=LittleClumsy_ToDo_CLI&metric=code_smells">
    <img src="https://sonarcloud.io/api/project_badges/measure?project=LittleClumsy_ToDo_CLI&metric=sqale_index">
    <img src="https://sonarcloud.io/api/project_badges/measure?project=LittleClumsy_ToDo_CLI&metric=vulnerabilities">
    <img src="https://sonarcloud.io/api/project_badges/measure?project=LittleClumsy_ToDo_CLI&metric=bugs">
</p>
<p align="center">
    <img src="https://sonarcloud.io/api/project_badges/measure?project=LittleClumsy_ToDo_CLI&metric=alert_status">
    <img src="https://sonarcloud.io/api/project_badges/measure?project=LittleClumsy_ToDo_CLI&metric=duplicated_lines_density">
</p>

## Installation 
PLEASE NOTE! ToDo_CLI is currently only working on Ubuntu 22.04.

### Installing ToDo using .exe.
When you install the todo.exe all the necessary files will be installed. 
Run ./todo in terminal to run the program.

```bash
./todo
```

### Using the source code.
When using the source code you need to unzip the downloaded file then you just need to run:

```bash
$ python todo.py
```

## Usage
To create a new task:

```bash
$ python todo.py create
```

When you want to view all your tasks:

```bash
$ python todo.py view
```
# Issues
We are aware of the problem where the program wont run if the config file already exists. We are looking at fixing it.

## License 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
