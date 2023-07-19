"""Subpackage to build training and inference pipelines
"""

import logging
import {{ cookiecutter.__repo_name }}.config as cfg
import {{ cookiecutter.__repo_name }}.dataset as dtst

logger = logging.getLogger(__name__)
logger.setLevel(cfg.log_level)

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
    # if necessary, preprocess data
    
    # choose AI model, load weights
    
    # return results of prediction
    predict_result = {'status': 'not implemented'}
    logger.debug(f"[predict()]: {predict_result}")

    return predict_result

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

    # return training results
    train_result = {'status': 'not implemented'}
    logger.debug(f"[train()]: {train_result}")
    
    return train_result
