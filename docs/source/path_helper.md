# Path helper

The path helper is responsible for handling paths. This is done primarily through the use of the OS module. 

## Get home directory function

The get home directory function is responsible for getting the home directory of the user. This function will return the path to the home directory as a string.

```python
>>> from todo_cli.helpers.path_helper import get_home_directory
>>> get_home_directory()
'/home/user'
```

## Create directory function

The create directory function is responsible for creating a directory. This function will return a boolean value that will be true if the directory was created and false if it was not created.

```python
>>> from todo_cli.helpers.path_helper import create_directory
>>> create_directory('/home/user/.todo')
True
```

## Join path function

The join path function is responsible for joining paths. This function will return the joined path as a string.

```python
>>> from todo_cli.helpers.path_helper import join_paths
>>> join_paths('/home/user', '.todo')
'/home/user/.todo'
```

## Path exists function

The path exists function is responsible for checking if a path exists. This function will return a boolean value that will be true if the path exists and false if it does not exist.

```python
>>> from todo_cli.helpers.path_helper import path_exists
>>> path_exists('/home/user/.todo')
True
```
