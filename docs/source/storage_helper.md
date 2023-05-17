# Storage Helper

The storage helper is responsible for handling the storage directory.

## What is the storage directory?

The storage directory is a directory that is used to store all of the data that is used by the program. This directory is created by the program and is located in the user's home directory. The storage directory is used to store the following:

* The config file
* The log file
* The tasks file

The storage directory will always be in a directory in the user's home directory. This directory will always be '.todo'. The storage directory will be created if it does not exist when the program is run.

## Get storage directory function

The get storage directory function is responsible for getting the storage directory. It will return the path to the storage directory even if it does not exist. This function will return the path to the storage directory as a string.

```python
>>> from todo_cli.helpers.storage_helper import get_storage_directory
>>> get_storage_directory()
'/home/user/.todo'
```

## Create storage directory function

The create storage directory function is responsible for creating the storage directory. This function will return a boolean value that will be true if the storage directory was created and false if it was not created.

```python
>>> from todo_cli.helpers.storage_helper import create_storage_directory
>>> create_storage_directory()
True
```

## More documentation

* [Path helper documentation](path_helper.md)
