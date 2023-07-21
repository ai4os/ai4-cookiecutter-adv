"""Endpoint functions to integrate your model with the DEEPaaS API.

For more information about how to edit the module see, take a look at the
docs [1] and at a canonical exemplar module [2].

[1]: https://docs.ai4eosc.eu/
[2]: https://github.com/deephdc/demo_app
"""
import logging
import time

from aiohttp.web import HTTPException

import {{ cookiecutter.__repo_name }} as aimodel

from . import config, responses, schemas, utils

logger = logging.getLogger(__name__)
logger.setLevel(config.log_level)


def get_metadata():
    """Returns a dictionary containing metadata information about the module.

    Raises:
        HTTPException: Unexpected errors aim to return 50X

    Returns:
        A dictionary containing metadata information required by DEEPaaS.
    """
    try:
        metadata = {
            "Author": [config.MODEL_METADATA.get("Author").replace('\"','')],
            "Author-email": [config.MODEL_METADATA.get("Author-email").replace('\"','')],
            "Description": config.MODEL_METADATA.get("Summary"),
            "License": config.MODEL_METADATA.get("License"),
            "Version": config.MODEL_METADATA.get("Version"),
            "Checkpoints": utils.ls_dirs(config.MODELS_PATH),
        }
        logger.debug("Package model metadata: %s", metadata)
        return metadata
    except Exception as err:
        raise HTTPException(reason=err) from err


#def warm():
#    """Function to run preparation phase before anything else can start"""


@utils.predict_arguments(schema=schemas.PredArgsSchema)
def predict(**options):
    """Performs model prediction from given input data and parameters.

    Arguments:
        **options -- Arbitrary keyword arguments from PredArgsSchema.

    Raises:
        HTTPException: Unexpected errors aim to return 50X

    Returns:
        The predicted model values or files.
    """
    logger.debug("Using options: %s", options)
    try:
        # call your AI model predict() method
        result = aimodel.predict(**options)
        return responses.content_types[options["accept"]](result, **options)
    except Exception as err:
        raise HTTPException(reason=err) from err


@utils.train_arguments(schema=schemas.TrainArgsSchema)
def train(**options):
    """Performs model training from given input data and parameters.

    Arguments:
        **options -- Arbitrary keyword arguments from TrainArgsSchema.

    Raises:
        HTTPException: Unexpected errors aim to return 50X

    Returns:
        Parsed history/summary of the training process.
    """
    logger.debug("Using options: %s", options)
    try:
        # call your AI model train() method
        result = aimodel.train(**options)
        return result
    except Exception as err:
        raise HTTPException(reason=err) from err
