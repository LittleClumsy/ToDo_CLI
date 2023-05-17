# Config controller

Config controller is responsible for installing and handling the configuration file.


## Get config path

This function will return the path to the config file.

```python
>>> from todo_cli.config.config_controller import get_config_path
>>> get_config_path()
'/home/user/.todo/config.json'
```

## Install config file

This function will install the config file if it doesn't exist.

Returns `True` if the config file was installed, `False` if it already existed.

```python
>>> from todo_cli.config.config_controller import install_config_file
>>> install_config_file()
True
```

## Read config file

This function will read the config file and return the config as a dictionary or list depending on the config file. It will raise an exception if the config file doesn't exist or if the config file is not valid JSON.

```python
>>> from todo_cli.config.config_controller import read_config_file
>>> read_config_file()
{'config': 'value'}
```

```python
>>> from todo_cli.config.config_controller import read_config_file
>>> read_config_file()
FileNotFoundError: Config file not found at /home/user/.todo/config.json
```

```python
>>> from todo_cli.config.config_controller import read_config_file
>>> read_config_file()
ValueError: Config file at /home/user/.todo/config.json is not valid JSON.
```

## Write config file

This function will write to the config file. It will raise an exception if the directory doesn't exist where the config file should be located.

```python
>>> from todo_cli.config.config_controller import write_config_file
>>> write_config_file({'config': 'value'})
None
```

```python
>>> from todo_cli.config.config_controller import write_config_file
>>> write_config_file({'config': 'value'})
FileNotFoundError: [Errno 2] No such file or directory: '/home/user/.todo/config.json'
```

## More documentation

[JSON Helper docs](json_helper.md)
[OS Helper docs](os_helper.md)