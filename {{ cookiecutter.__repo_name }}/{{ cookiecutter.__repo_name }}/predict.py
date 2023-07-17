"""Module to build inference pipeline
"""

import logging
# import package config.py
import {{ cookiecutter.__repo_name }}.config as cfg

logger = logging.getLogger(__name__)


def predict(**kwargs):
    """Main function to configure inference/prediction
    """
    inference_result = {}
    
    return inference_result