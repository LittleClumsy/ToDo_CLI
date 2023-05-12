# Todo.py

todo.py is the entry point file for the todo application. It is responsible for installing the required files and passing along the cli-arguments to the appropriate functions. It will also handle the exit codes.

## Command line arguments

todo.py uses the `sys` package to retrieve the command line arguments. It will then pass the arguments to the appropriate function.

We remove the first argument before it gets passed to our main function. This is because the first argument is always the name of the script.

## More documentation

* [Exit codes](../misc/exit_codes.md)

