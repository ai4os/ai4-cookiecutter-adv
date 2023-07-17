"""Module to prepare the dataset
"""
import logging
from pathlib import Path
# import package config.py
import {{ cookiecutter.__repo_name }}.config as cfg

logger = logging.getLogger(__name__)

def make_dataset(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed.
    """

    logger.info('Making final data set from raw data')

    # EXAMPLE for finding various files
    project_dir = Path(__file__).resolve().parents[2]


