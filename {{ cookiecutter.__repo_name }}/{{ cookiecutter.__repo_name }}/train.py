"""Module to build training pipeline
"""

import logging
# import package config.py
import {{ cookiecutter.__repo_name }}.config as cfg
import {{ cookiecutter.__repo_name }}.dataset.make_dataset as make_dataset
import {{ cookiecutter.__repo_name }}.model.create_model as create_model

logger = logging.getLogger(__name__)


def train(**kwargs):
    """Main function to configure training (e.g. which model to use)
    """
    # prepare the dataset
    
    # create model
    
    # train model
    
    train_result = {}
    
    return train_result
    