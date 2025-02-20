# python-challenge

Repository for technical interviews

Fork this repository and share with me (@kingledion). When we're done with the code challenge I'd like you to commit the code to your fork so I can take a look at it again later to refresh my memory. Please, no changes after we are finished with the live challenge. 

## Prerequisites

- Install [`pyenv`](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation) for Python veresion management
- Use pyenv make Python version available for current version; e.g. `pyenv install 3.12`
    - NOTE: there is an issue with `3.12.5`; tested working with `3.12.6` and `3.12.9`. 
- Install [`poetry`](https://python-poetry.org/docs/#installation)

## Development setup

Dependencies and virtual environments are managed using [Poetry](https://python-poetry.org/). For first time use, set python environment and dependencies:
  ```bash
  $ pyenv local 3.12
  $ poetry env use 3.12
  $ poetry install
  ```

This should activate the appropriate python environment and install all dependencies through `poetry`. 

## Lint

Linting is set up using the following linters:
 - black
 - isort
 - flake8
 - mypy

### VSCode setup

If using VSCode, the following extensions can be installed to enforce linting:
 - Black Formatter by Microsoft
 - Flake8 by Microsoft
 - Mypy Type Checker by Microsoft
 - Pylance by Microsoft
 - Python by Microsoft

In addition, `mypy` will recognize the configuration in `.mypy.ini` if the following is set in `.vscode/settings.json`:

```json
{
    "mypy-type-checker.args": ["--config-file=${workspaceFolder}/.mypy.ini"],
    "mypy-type-checker.reportingScope": "workspace"
}
```

This isn't strictly necessary for the code challenge, but it will help keep everything looking clean and error free. 

## Unit testing

Unit testing is run using `make test`. 

## Run locally
- This example is designed to run with its own SQLite database to avoid issues with setting up any dependencies. A user is auto-populated with the startup in main so that notifications can be tested. 

- Run the server locally with `make server`

- Test locally using the rest commands in  `test.rest.http`. These are designed to work with the VSCode plugin "REST Client" by Huchao Mao, but can easily be converted to CURL commands.