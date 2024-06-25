# {{cookiecutter.__repo_name}}

[![Build Status](https://jenkins.services.ai4os.eu/buildStatus/icon?job=AI4OS-hub/{{ cookiecutter.__repo_name }}/main)](https://jenkins.services.ai4os.eu/job/AI4OS-hub/job/{{ cookiecutter.__repo_name }}/job/main/)

{{cookiecutter.description}}

To launch it, first install the package then run [deepaas](https://github.com/ai4os/DEEPaaS):

> ![warning](https://img.shields.io/badge/Warning-red.svg) **Warning**: If you are using a virtual environment, make sure you are working with the last version of pip before installing the package. Use `pip install --upgrade pip` to upgrade pip.

```bash
git clone {{ cookiecutter.git_base_url }}/{{ cookiecutter.__repo_name }}
cd {{ cookiecutter.__repo_name }}
pip install -e .
deepaas-run --listen-ip 0.0.0.0
```

## Project structure

```
├── Jenkinsfile             <- Describes basic Jenkins CI/CD pipeline
├── Dockerfile              <- Steps to build a DEEPaaS API Docker image
├── LICENSE                 <- License file
├── README.md               <- The top-level README for developers using this project.
├── VERSION                 <- Version file indicating the version of the model
│
├── {{ cookiecutter.__app_name }}
│   ├── README.md           <- Instructions on how to integrate your model with DEEPaaS.
│   ├── __init__.py         <- Makes <your-model-source> a Python module
│   ├── ...                 <- Other source code files
│   └── config.py           <- Module to define CONSTANTS used across the AI-model python package
│
├── api                     <- API subpackage for the integration with DEEP API
│   ├── __init__.py         <- Makes api a Python module, includes API interface methods
│   ├── config.py           <- API module for loading configuration from environment
│   ├── responses.py        <- API module with parsers for method responses
│   ├── schemas.py          <- API module with definition of method arguments
│   └── utils.py            <- API module with utility functions
│
├── data                    <- Data subpackage for the integration with DEEP API
│
├── docs                    <- A default Sphinx project; see sphinx-doc.org for details
│
├── models                  <- Folder to store your models
│
├── notebooks               <- Jupyter notebooks. Naming convention is a number (for ordering),
│                              the creator's initials (if many user development),
│                              and a short `_` delimited description, e.g.
│                              `1.0-jqp-initial_data_exploration.ipynb`.
│
├── references              <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports                 <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures             <- Generated graphics and figures to be used in reporting
│
├── requirements-dev.txt    <- Requirements file to install development tools
├── requirements-test.txt   <- Requirements file to install testing tools
├── requirements.txt        <- Requirements file to run the API and models
│
├── pyproject.toml          <- Makes project pip installable (pip install -e .)
│
├── tests                   <- Scripts to perform code testing
│   ├── configurations      <- Folder to store the configuration files for DEEPaaS server
│   ├── conftest.py         <- Pytest configuration file (Not to be modified in principle)
│   ├── data                <- Folder to store the data for testing
│   ├── models              <- Folder to store the models for testing
│   ├── test_deepaas.py     <- Test file for DEEPaaS API server requirements (Start, etc.)
│   ├── test_metadata       <- Tests folder for model metadata requirements
│   ├── test_predictions    <- Tests folder for model predictions requirements
│   └── test_training       <- Tests folder for model training requirements
│
└── tox.ini                 <- tox file with settings for running tox; see tox.testrun.org
```

## Integrating your model with DEEPaaS

After executing the cookiecutter template, you will have a folder structure
ready to be integrated with DEEPaaS. The you can decide between starting the
project from scratch or integrating your existing model with DEEPaaS.

The folder `{{ cookiecutter.__app_name }}` is designed to contain the source
code of your model. You can add your model files there or replace it by another
repository by using [git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules).
The only requirement is that the folder `{{ cookiecutter.__app_name }}` contains
an `__init__.py` file conserving the already defined methods. You can edit the
template functions already defined inside or import your own functions from
another file. See the [README.md](./{{ cookiecutter.__app_name }}/README.md)
in the `{{ cookiecutter.__app_name }}` folder for more information.

Those methods, are used by the subpackage `api` to define the API interface.
See the project structure section for more information about the `api` folder.
You are allowed to customize your model API and CLI arguments and responses by
editing `api.schemas` and`api.responses` modules. See documentation inside those
files for more information.

Sometimes you only need to add an interface to an existing model. In case that
the model is already published in a public repository, you can add it as a
requirement into the `requirements.txt` file. If the model is not published
yet, you can add it as a submodule inside or outside the project and install
it by using `pip install -e <path-to-model>`. In both cases, you will need to
interface the model with the `api` subpackage with the required methods. See
the [README.md](./{{ cookiecutter.__app_name }}/README.md)

## Documentation

TODO: Add instructions on how to build documentation

## Testing

Testing process is automated by tox library. You can check the environments
configured to be tested by running `tox --listenvs`. If you are missing one
of the python environments configured to be tested (e.g. py310, py39) and
you are using `conda` for managing your virtual environments, consider using
`tox-conda` to automatically manage all python installation on your testing
virtual environment.

Tests are implemented following [pytest](https://docs.pytest.org) framework.
Fixtures and parametrization are placed inside `conftest.py` files meanwhile
assertion tests are located on `test_*.py` files. As developer, you can edit
any of the existing files or add new ones as needed. However, the project is
designed so you only have to edit the files inside:

    - tests/data: To add your testing data (small datasets, etc.).
    - tests/models: To add your testing models (small models, etc.).
    - tests/test_metadata: To fix and test your metadata requirements.
    - tests/test_predictions: To fix and test your predictions requirements.
    - tests/test_training: To fix and test your training requirements.

The folder `tests/data` should contain minimalistic but representative
datasets to be used for testing. In a similar way, `tests/models` should
contain simple models for testing that can fit on your code repository. This
is important to avoid large files on your repository and to speed up the
testing process.

Running the tests with tox:

```bash
$ pip install -r requirements-dev.txt
$ tox
```

Running the tests with pytest:

```bash
$ pip install -r requirements-test.txt
$ python -m pytest --numprocesses=auto --dist=loadscope tests
```
