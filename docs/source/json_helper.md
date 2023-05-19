# JSON Helper

This module is used to help with the reading and writing of JSON files.

## Write json file

This function is used to write a dictionary or list to a json file. If the file does not exist it will be created. If the file does exist it will be overwritten. If you give the function a value that is not of type dictionary or list it will raise a `TypeError`.

```python
>>> from todo_cli.helpers.json_helper import write_json_file
>>> write_json_file('test.json', {'test': 'test'})
None
```

```python
>>> from todo_cli.helpers.json_helper import write_json_file
>>> write_json_file('test.json', ['test', 'test'])
None
```

```python
>>> from todo_cli.helpers.json_helper import write_json_file
>>> write_json_file('test.json', 'test')
TypeError
```

## Read json file

This function is used to read a json file and return the contents as a dictionary or list. If the file does not exist it will raise a `FileNotFoundError`. If the file does exist and is not empty it will return the contents of the file as a dictionary or list. If the file does exist but it does not contain json that can be converted to a list or dictionary it will raise a `TypeError`.

```python
>>> from todo_cli.helpers.json_helper import read_json_file
>>> read_json_file('test.json')
{'test': 'test'}
```

```python
>>> from todo_cli.helpers.json_helper import read_json_file
>>> read_json_file('test.json')
['test', 'test']
```

```python
>>> from todo_cli.helpers.json_helper import read_json_file
>>> read_json_file('test.json')
FileNotFoundError
```

```python
>>> from todo_cli.helpers.json_helper import read_json_file
>>> read_json_file('test.json')
TypeError
```
