# Todo.py

todo.py is the entry point file for the todo application. It is responsible for installing the required files and passing along the cli-arguments to the appropriate functions. It will also handle the exit codes.

## Command line arguments

todo.py uses the `sys` package to retrieve the command line arguments. It will then pass the arguments to the appropriate function.

We remove the first argument before it gets passed to our main function. This is because the first argument is always the name of the script.

## Main function

The main function is responsible for calling the appropriate function based on the command line arguments. It will also handle the exit codes. This is the entry point of the application.

## Install app function

The install app function is responsible for installing the required files for the todo application. It will create the required directories and files.

This function can raise the following exceptions:
* FileNotFoundError - If the directory for installation does not exist, this will only happen if the installation for the directory fails.

## Handle install error function

The handle install error function is responsible for handling the errors that occur during installation. It will print the error message and return the appropriate exit code.

## More documentation

* [Exit codes](../misc/exit_codes.md)
* [CLI Controller Docs](cli_controller.md)
* [Config Controller Docs](config_controller.md)
* [Storage Helper Docs](storage_helper.md)
* [Tasks Helper Docs](tasks_helper.md)
* [Logger Docs](logger.md)

