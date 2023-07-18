"""Configuration loader for DEEPaaS API."""
import os
from importlib.metadata import metadata as _metadata
from pathlib import Path, PurePath

# base path for the local repository
BASE_PATH = Path(__file__).resolve().parents[1]
# default path for the data
DATA_PATH = Path(os.getenv("DATA_PATH", default=PurePath(BASE_PATH,"data")))
# default path for the pre-trained models
MODELS_PATH = Path(os.getenv("MODELS_PATH", default=PurePath(BASE_PATH,"models")))

# default AI model
MODEL_NAME = os.getenv("MODEL_NAME", default="{{ cookiecutter.__repo_name }}")

# get AI model metadata
MODEL_METADATA = _metadata(MODEL_NAME) #.json
# Author seems to be not correctly extracted, see e.g.
# https://stackoverflow.com/questions/75249518/right-way-to-publish-authors-on-pypi-from-setuptools/75361691#75361691
if 'Author' not in MODEL_METADATA.keys():
    MODEL_METADATA['Author'] = MODEL_METADATA['Author-email'].split()[0]
