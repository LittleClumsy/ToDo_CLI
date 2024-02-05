# tasks docs

## Table of Contents

* [Introduction](#introduction)
* [Commands](#commands)

## Introduction

This document will explain how to use the CLI commands. 

## Commands

Listed below are the available commands for Todo_CLI. Typer will also allow you use the '--help' command to view the available commands for you to use.

### Create

This command is used to create a new task. You can use the create command as follows, just replace 'run' and '2023' with your own task and date.

```bash
python todo.py create --name run --date 2023
```

If you use Typer you will be prompted for the name of the task and the date.

```bash
python todo.py create
```

### View

This command is used to view existing tasks.

```bash
python todo.py view
```

### Edit

This command is used to edit an existing task. 'id' is the UUID of the task which you can get by first viewing your existing tasks and copying the UUID of the task you would like to edit. 'field' is the field of the task you would like to edit, eg. 'name' or 'date'. 'value' is the new task or date you would like to replace the old with.

```bash
python todo.py edit --id abcd123 --field name --value Laundry
```

You can also use typer for the edit command. You will be prompted for the id, field name and value.

```bash
python todo.py edit
```


### Delete

This command is used to delete tasks. You can use the following command to delete a single task by replaceing 'UUID' with the tasks UUID: 

```bash
python todo.py delete one UUID
```

You can also use the following command to delete multiple tasks at once:

```bash
python todo.py delete many 'UUID' 'UUID'....
```



