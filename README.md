<div align="center">
  <img src="https://ai4eosc.eu/wp-content/uploads/sites/10/2022/09/horizontal-transparent.png" alt="logo" width="500"/>
</div>

# AI4OS Hub Modules Template (advanced)

## For users

This is an advanced template for developing new modules in the AI4OS Platform. It uses [Cookiecutter](https://cookiecutter.readthedocs.io) to generate the templates. This template is based on the  [Cookiecutter Data Science](http://drivendata.github.io/cookiecutter-data-science/) template. It makes more assumptions on how to structure projects and adds more files compared to the "main" version. If you want to integrate an already existing AI code, which you still want to keep in a separate repository, this template is for you.

There are different versions of the template:

* [main](https://github.com/ai4os/ai4-template): this is a minimal version of the AI4OS Hub template: Simple template, with the minimum requirements to integrate your AI model in AI4OS Hub.

* [child-module](https://github.com/ai4os/ai4-template-child): this template specifically tailors to users performing a retraining of an existing at AI4OS-Hub module. It only creates a Docker repo whose container is based on an existing module's Docker image.

To create a new template of your project, either

* install cookiecutter and run it with this template: 
``` bash
pip install cookiecutter
cookiecutter https://github.com/ai4os/ai4-template-adv.git
```
* OR visit our Templates Hub service: https://templates.cloud.ai4eosc.eu/ and select the template
```

With the advanced template, there are 3 different options to implement your project:

1. `Add model template` (default): This option will create in the template a folder with the basic structure to implement your model.
2. `Add model from repository`: This option will import your model from a git repository as submodule. You will need to introduce the git repository URL.
3. `Model in requirements.txt`: If you do not want the model source code in the repository (via any of the last 2 options), you can add the model package to `requirements.txt` file.

> For options 2 and 3, you need to edit or ensure the variables required by the API module are available, e.i. `DATA_PATH` and `MODELS_PATH`.

Once you answer all the questions, the project directory will be created as a git repository with two branches: `master` and `test`.
This is what the folder structures look like:

## Project structure

```
├── Jenkinsfile             <- Describes basic Jenkins CI/CD pipeline
├── Dockerfile              <- Steps to build a DEEPaaS API Docker image
├── LICENSE                 <- License file
├── README.md               <- The top-level README for developers using this project.
├── VERSION                 <- Version file indicating the version of the model
│
├── <your-model-source>     <- Source code for use in this project.
|   |                          (only if add_model_template/from_repo)
│   ├── README.md           <- Model README for developers using this model.
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

More extended documentation can be found [here](http://docs.deep-hybrid-datacloud.eu/en/latest/user/overview/cookiecutter-template.html).
If you want to look at a minimal app using this template structure check [demo-advanced](https://github.com/ai4os-hub/demo-advanced).

Run the cookiecutter tests with `python -m pytest tests`.

## For developers

Once you update the template, please, update this `README.md`, and **especially** `cookiecutter.json` file and `"__ai4_template"` entry with the corresponging, incremented version. The convention for the `"__ai4_template"` entry is to provide the template repository name, slash '/' closest version of the template, following [SymVer](https://semver.org/) specs, e.g.

```
"__ai4_template": "ai4-template/2.1.0"
```
OR
```
"__ai4_template": "ai4-template-adv/2.1.0"
```
OR
```
"__ai4_template": "ai4-template-child/2.1.0"