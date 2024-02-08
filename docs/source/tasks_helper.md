# [Tasks Helper](../../todo_cli/helpers/tasks_helper.py)

Tasks helper is responsible for creating, viewing, updating, and deleting tasks. It is also contains the logic for writing and reading tasks to and from the tasks file aswell as installing the tasks file.

## Install tasks file function

The install tasks file function is responsible for installing the tasks file. This function will return a boolean value that will be true if the tasks file was installed and false if it was not installed.

```python
>>> from todo_cli.helpers.tasks_helper import install_tasks_file
>>> install_tasks_file()
True
```

## Read tasks file function

The read tasks file function is responsible for reading the tasks file. This function will return the tasks file as a list.

```python
>>> from todo_cli.helpers.tasks_helper import read_tasks_file
>>> read_tasks_file()
[
    {"task #1": "This is task #1"},
    {"task #2": "This is task #2"},
    {"task #3": "This is task #3"}
]
```

## Write tasks file function

The write tasks file function is responsible for writing the tasks file. This function will return a boolean value that will be true if the tasks file was written and false if it was not written.

```python
>>> from todo_cli.helpers.tasks_helper import write_tasks_file
>>> write_tasks_file([
    {"task #1": "This is task #1"},
    {"task #2": "This is task #2"},
    {"task #3": "This is task #3"}
])
```

## Create task function

The create task function is responsible for creating a task and returning it as a dictionary. It does not save the task to the tasks file. It will create it for you to add it to the tasks file.

```python
>>> from todo_cli.helpers.tasks_helper import create_task
>>> create_task('This is a task')
{'This is a task': 'This is a task'}
```

## Validate task function

The validate task function is responsible for validating that the given id's exist in your task file. It will return a boolean value that will only be True if all the given task id's exist in your tasks.json file.

```python
>>> from todo_cli.helpers.tasks_helper import validate_task_ids
>>> validate_task_ids()
False
```

## Delete task function

This function is responsible for deleting tasks. Once this function validates that the provided id(s) exist in the tasks file it will delete the task. 

```python
>>> from todo_cli.helpers.tasks_helper import validate_task_ids
>>> delete_task(['123'])
Deleted task with ID(s): ['123']
```


