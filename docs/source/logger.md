# [Logger](../../todo_cli/logs/logger.py)

The logger is responsible for logging messages to a text file. This is so that there is always info as to what is happening and when errors happened, the text file might be able to help you figure out what went wrong. This is to help developers debug the application.

## Log function

The log function is responsible for logging messages to a text file. This function will return a boolean value that will be true if the message was logged and false if it was not logged.

```python
>>> from todo_cli.logs.logger import create_log
>>> create_log('This is a message')
```