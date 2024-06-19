"""Package to create datasets, pipelines and other utilities.

You can use this module for example, to write all the functions needed to
operate the methods defined at `__init__.py` or in your scripts.

All functions here are optional and you can add or remove them as you need.
"""
import logging
from pathlib import Path
from {{ cookiecutter.__app_name }} import config

logger = logging.getLogger(__name__)
logger.setLevel(config.LOG_LEVEL)


# make data
# = HAVE TO MODIFY FOR YOUR NEEDS =
def mkdata(input_filepath, output_filepath):
    """ Main/public function to run data processing to turn raw data
        from (data/raw) into cleaned data ready to be analyzed.
    """

    logger.info('Making final data set from raw data')

    # EXAMPLE for finding various files
    project_dir = Path(__file__).resolve().parents[2]


# create model
# = HAVE TO MODIFY FOR YOUR NEEDS =
def create_model(**kwargs):
    """Main/public method to create AI model
    """
    # define model parameters
    
    # build model based on the deep learning framework
    
    return model

