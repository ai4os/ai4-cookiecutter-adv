"""Subpackage to build training and inference pipelines
"""

import logging
import {{ cookiecutter.__repo_name }}.config as cfg
import {{ cookiecutter.__repo_name }}.dataset as dtst

logger = logging.getLogger(__name__)

# create model
def create_model(**kwargs):
    """Main/public method to create AI model
    """
    # define model parameters
    
    # build model based on the deep learning framework
    
    return model

# predict
def predict(**kwargs):
    """Main/public method to perform prediction
    """
    inference_result = {}
    
    return inference_result

# train
def train(**kwargs):
    """Main/public method to perform training
    """
    # prepare the dataset, e.g.
    # dtst.mkdata()
    
    # create model, e.g.
    # create_model()
    
    # train model
    # describe training steps

    train_result = {}
    
    return train_result
