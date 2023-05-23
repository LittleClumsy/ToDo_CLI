# Errors

Please refer to [Exit code docs](../misc/exit_codes.md) for more information on exit codes.

## Handle install error

This function is used to handle errors that occur during the installation of the application. It will print the error message and return exit code 1.

```python
>>> from todo_cli.helpers.error import handle_install_error
>>> error = Exception("This should be a install error")
>>> handle_install_error(error)
This should be a install error.
Install Error [1]: Could not create storage directory or files.
Please report this issue to the developer.
```

## Handle json error

This function is used to handle errors that occur when reading or writing to a JSON file. It will print the error message and return exit code 2.

```python
>>> from todo_cli.helpers.error import handle_json_error
>>> error = Exception("This should be a json error")
>>> handle_json_error(error)
This should be a json error.
JSON Error [2]: Please report this issue to the developer.
```