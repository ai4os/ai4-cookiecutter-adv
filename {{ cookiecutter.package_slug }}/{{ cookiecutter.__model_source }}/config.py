"""Module to define CONSTANTS used across the AI-model package.

This module is used to define CONSTANTS used across the AI-model package.
Do not misuse this module to define variables that are not CONSTANTS or
exclusive to the {{ cookiecutter.__model_source }} package. You can use the `config.py`
inside `api` to define exclusive CONSTANTS related to your interface.

By convention, the CONSTANTS defined in this module are in UPPER_CASE.
"""
# Do NOT import anything from `api` or `{{ cookiecutter.__model_source }}` packages here.
# That might create circular dependencies.
import logging
import os
from pathlib import Path

# DEEPaaS can load more than one installed models. Therefore, in order to
# avoid conflicts, each default PATH environment variables should lead to
# a different folder. The current practice is to use the path from where the
# model source is located.
BASE_PATH = Path(__file__).resolve(strict=True).parents[1]

# Path definition for the pre-trained models
MODELS_PATH = os.getenv("{{ cookiecutter.__model_source|upper }}_MODELS_PATH", default=BASE_PATH / "models")
MODELS_PATH = Path(MODELS_PATH)
# Path definition for data folder
DATA_PATH = os.getenv("{{ cookiecutter.__model_source|upper }}_DATA_PATH", default=BASE_PATH / "data")
DATA_PATH = Path(DATA_PATH)

# configure logging:
# logging level across various modules can be setup via USER_LOG_LEVEL,
# options: DEBUG, INFO(default), WARNING, ERROR, CRITICAL
ENV_LOG_LEVEL = os.getenv("{{ cookiecutter.__model_source|upper }}_LOG_LEVEL", "INFO")
LOG_LEVEL = getattr(logging, ENV_LOG_LEVEL.upper())

# EXAMPLE on how to load environment variables
PARAMETER_INT = int(os.getenv("{{ cookiecutter.__model_source|upper }}_PARAMETER_INT", default="10"))
