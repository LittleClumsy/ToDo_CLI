# Git Ignore

The `.gitignore` file is a plain text file where each line contains a pattern for files/directories to ignore. Generally, this is placed in the root folder of the repository, and that's what we do here.

## Template

We use the python gitignore template from github.

## Additions

We add the following to the .gitignore file:

```gitignore
# IDE/Editor settings
.vscode/
```

We ignore ide settings as this is a personal preference and should not be shared with the team.