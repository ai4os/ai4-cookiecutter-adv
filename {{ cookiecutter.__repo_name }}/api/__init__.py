"""Endpoint functions to integrate your model with the DEEPaaS API.

For more information about how to edit the module see, take a look at the
docs [1] and at a canonical exemplar module [2].

[1]: https://docs.deep-hybrid-datacloud.eu/
[2]: https://github.com/deephdc/demo_app
"""
import logging
import time

import tensorflow as tf
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
            "Author": [config.MODEL_METADATA.get("Author")],
            "Author-email": [config.MODEL_METADATA.get("Author-email")],
            "Summary": config.MODEL_METADATA.get("Summary"),
            "License": config.MODEL_METADATA.get("License"),
            "Version": config.MODEL_METADATA.get("Version"),
            "Checkpoints": utils.ls_models(),
            "Datasets": utils.ls_datasets(),
        }
        logger.debug("Package model metadata: %s", metadata)
        return metadata
    except Exception as err:
        raise HTTPException(reason=err) from err


@utils.predict_arguments(schema=schemas.PredArgsSchema)
def predict(checkpoint, input_file, accept, **options):
    """Performs {model} prediction from given input data and parameters.

    Arguments:
        checkpoint -- Model from checkpoint to use for predicting values.
        input_file -- Input data file to perform predictions from model.
        accept -- Response parser type.
        **options -- Arbitrary keyword arguments from PredArgsSchema.

    Options:
        batch_size -- Number of samples per batch.
        steps -- Steps before prediction round is finished.

    Raises:
        HTTPException: Unexpected errors aim to return 50X

    Returns:
        The predicted model values or files.
    """
    try:
        logger.debug("Using model %s for predictions", checkpoint)
        model = tf.keras.models.load_model(checkpoint)
        logger.debug("Predictions from input_file: %s", input_file)
        logger.debug("Using options: %s", options)
        result = aimodel.predict(model, input_file.filename, **options)
        logger.debug("Using parser for: %s", accept)
        return responses.content_types[accept](result)
    except Exception as err:
        raise HTTPException(reason=err) from err


@utils.train_arguments(schema=schemas.TrainArgsSchema)
def train(checkpoint, dataset, **options):
    """Performs {model} training from given input data and parameters.

    Arguments:
        checkpoint -- Model from checkpoint to train with the input files.
        dataset -- Dataset name with images and labels to use for training.
        **options -- Arbitrary keyword arguments from TrainArgsSchema.

    Options:
        epochs -- Number of epochs to train the model.
        initial_epoch -- Epoch at which to start training.
        steps_per_epoch -- Steps before declaring an epoch finished.
        shuffle -- Shuffle the training data before each epoch.
        validation_split -- Fraction of the data to be used as validation.
        validation_steps -- Steps to draw before stopping on validation.
        validation_batch_size -- Number of samples per validation batch.
        validation_freq -- Training epochs to run before validation.

    Raises:
        HTTPException: Unexpected errors aim to return 50X

    Returns:
        Parsed history/summary of the training process.
    """
    try:
        logger.debug("Using model %s for training", checkpoint)
        model = tf.keras.models.load_model(checkpoint)
        logger.debug("Training from dataset: %s", dataset)
        ckpt_name = f"{time.strftime('%Y%m%d-%H%M%S')}.cp.ckpt"
        options["callbacks"] = utils.generate_callbacks(ckpt_name)
        logger.debug("Using options: %s", options)
        result = aimodel.train(model, dataset, **options)
        return {"new_checkpoint": ckpt_name, **result.history}
    except Exception as err:
        raise HTTPException(reason=err) from err
