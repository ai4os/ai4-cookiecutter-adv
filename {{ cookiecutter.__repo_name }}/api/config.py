"""Module to define CONSTANTS used across the DEEPaaS Interface.

This module is used to define CONSTANTS used across the API interface.
Do not misuse this module to define variables that are not CONSTANTS or
that are not used across the `api` package. You can use the `config.py`
file on your model package to define CONSTANTS related to your model.

By convention, the CONSTANTS defined in this module are in UPPER_CASE.
"""
import logging
import os
from importlib import metadata

# Ensure that your model package has a config.py file with the following
# pylint: disable=unused-import
from {{ cookiecutter.__app_name }}.config import DATA_PATH, MODELS_PATH

# Get AI model metadata
API_NAME = "{{ cookiecutter.__app_name }}"
API_METADATA = metadata.metadata(API_NAME)  # .json

# Fix metadata for emails from pyproject parsing
_EMAILS = API_METADATA["Author-email"].split(", ")
_EMAILS = map(lambda s: s[:-1].split(" <"), _EMAILS)
API_METADATA["Author-emails"] = dict(_EMAILS)

# Fix metadata for authors from pyproject parsing
_AUTHORS = API_METADATA.get("Author", "").split(", ")
_AUTHORS = [] if _AUTHORS == [""] else _AUTHORS
_AUTHORS += API_METADATA["Author-emails"].keys()
API_METADATA["Authors"] = sorted(_AUTHORS)

# logging level across API modules can be setup via API_LOG_LEVEL,
# options: DEBUG, INFO(default), WARNING, ERROR, CRITICAL
ENV_LOG_LEVEL = os.getenv("API_LOG_LEVEL", default="INFO")
LOG_LEVEL = getattr(logging, ENV_LOG_LEVEL.upper())
