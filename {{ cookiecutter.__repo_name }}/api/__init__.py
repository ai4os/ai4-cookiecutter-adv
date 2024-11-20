"""Endpoint functions to integrate your model with the DEEPaaS API.

For more information about how to edit the module see, take a look at the
docs [1] and at a canonical exemplar module [2].

[1]: https://docs.ai4eosc.eu/
[2]: https://github.com/ai4os-hub/demo-advanced
"""
import logging

import {{ cookiecutter.__app_name }} as aimodel

from . import config, responses, schemas, utils

logger = logging.getLogger(__name__)
logger.setLevel(config.LOG_LEVEL)


def get_metadata():
    """Returns a dictionary containing metadata information about the module.

    Raises:
        HTTPException: Unexpected errors aim to return 50X

    Returns:
        A dictionary containing metadata information required by DEEPaaS.
    """
    try:  # Call your AI model metadata() method
        logger.info("Collecting metadata from: %s", config.API_NAME)
        metadata = config.PROJECT_METADATA
        # TODO: Add dynamic metadata collection here
        logger.debug("Package model metadata: %s", metadata)
        return metadata
    except Exception as err:
        logger.error("Error collecting metadata: %s", err, exc_info=True)
        raise  # Reraise the exception after log


def warm():
    """Function to run preparation phase before anything else can start.

    Raises:
        RuntimeError: Unexpected errors aim to stop model loading.
    """
    try:  # Call your AI model warm() method
        logger.info("Warming up the model.api...")
        aimodel.warm()
    except Exception as err:
        logger.error("Error when warming up: %s", err, exc_info=True)
        raise RuntimeError(reason=err) from err


@utils.predict_arguments(schema=schemas.PredArgsSchema)
def predict(model_name, input_file, accept='application/json', **options):
    """Performs model prediction from given input data and parameters.

    Arguments:
        model_name -- Model name from registry to use for prediction values.
        input_file -- File with data to perform predictions from model.
        accept -- Response parser type, default is json.
        **options -- Arbitrary keyword arguments from PredArgsSchema.

    Raises:
        HTTPException: Unexpected errors aim to return 50X

    Returns:
        The predicted model values (dict or str) or files.
    """
    try:  # Call your AI model predict() method
        logger.info("Using model %s for predictions", model_name)
        logger.debug("Loading data from input_file: %s", input_file.filename)
        logger.debug("Predict with options: %s", options)
        result = aimodel.predict(model_name, input_file.filename, **options)
        logger.debug("Predict result: %s", result)
        logger.info("Returning content_type for: %s", accept)
        return responses.content_types[accept](result, **options)
    except Exception as err:
        logger.error("Error calculating predictions: %s", err, exc_info=True)
        raise  # Reraise the exception after log


@utils.train_arguments(schema=schemas.TrainArgsSchema)
def train(model_name, input_file, **options):
    """Performs model training from given input data and parameters.

    Arguments:
        model_name -- Model name from registry to use for training values.
        input_file -- File with data and labels to use for training.
        **options -- Arbitrary keyword arguments from TrainArgsSchema.

    Raises:
        HTTPException: Unexpected errors aim to return 50X

    Returns:
        Parsed history/summary of the training process.
    """
    try:  # Call your AI model train() method
        logger.info("Using model %s for training", model_name)
        logger.debug("Loading data from input_file: %s", input_file)
        logger.debug("Training with options: %s", options)
        result = aimodel.train(model_name, input_file, **options)
        logger.debug("Training result: %s", result)
        return result
    except Exception as err:
        logger.error("Error while training: %s", err, exc_info=True)
        raise  # Reraise the exception after log

