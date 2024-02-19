# CLI Controller

This module is used to help with CLI commands.

## Create

The create function is used to create a new task. There will be a prompt in the terminal for a 'name', 'date' and 'priority'. A UUID will be generated for the task. These values get passed into the adding_content function to add it to the existing tasks.


## View

This function is used to view existing tasks. It uses Tabulate to view the tasks in a table format.

## Edit

The edit function allows you to edit existing tasks. It will prompt for an id(the UUID of the task you want to edit), field_name(The field you want to edit eg. name or date) and value (The new value you want to replace it with). It wont allow you to edit the id of a task, neither edit a field that does not exist.

```python
>>> from todo_cli.cli.cli_controller import edit
>>> edit('abcd1234', 'name', 'Run')
None
```

```python
>>> from todo_cli.cli.cli_controller import edit
>>> edit('abcd1234', 'id', 'Run')
Invalid field. The id can not be edited.
```

```python
>>> from todo_cli.cli.cli_controller import edit
>>> edit('abcd1234', 'Hello', 'Run')
That field does not exist! Please select a valid field to edit.
```

## Adding content

This function works with the create function to add new tasks to tasks.json file. 

## Delete

The delete function allows you to delete tasks. There are 2 options when it comes to deleting tasks:
delete_one - for deleting a single task.  

```python
>>> from todo_cli.cli.cli_controller import delete_one
>>> delete_one('123')
Deleted task with ID(s): ['123']
```

```python
>>> from todo_cli.cli.cli_controller import delete_one
>>> delete_one()
Please provide an ID
```

```python
>>> from todo_cli.cli.cli_controller import delete_one
>>> delete_one('123', '456')
Can not delete more than 1 task at a time.
```

The second option is delete_many.

```python
>>> from todo_cli.cli.cli_controller import delete_many
>>> delete_many('123', '456')
Deleted task with ID(s): ['123', '456']
``` 

```python
>>> from todo_cli.cli.cli_controller import delete_many
>>> delete_many('123')
Please provide at least 2 task id's to delete.
``` 

## Export

The Export function allows you to export your data. There are 2 options when it comes to exporting:
Exporting to JSON file:

```python
>>> from todo_cli.cli.cli_controller import export
>>> export("json", "file_name.json")
File exported as .json file.
```

Exporting to CSV file:

```python
>>> from todo_cli.cli.cli_controller import export
>>> export("csv", "file_name.csv")
File exported as .csv file.
```