"""Utilities module for API endpoints and methods.
"""
import logging
import sys

from keras import callbacks

from . import config

logger = logging.getLogger(__name__)


def ls_models():
    """Utility to return a list of models available in `models` folder.

    Returns:
        A list of strings in the format {submodel}-{timestamp}.
    """
    logger.debug("Scanning at: %s", config.MODELS_PATH)
    dirscan = (x.name for x in config.MODELS_PATH.iterdir() if x.is_dir())
    return sorted(dirscan)


def ls_datasets():
    """Utility to return a list of datasets available in `data` folder.

    Returns:
        A list of strings in the format {id}-{type}.npz.
    """
    logger.debug("Scanning at: %s", config.DATA_PATH)
    dirscan = (x.name for x in config.DATA_PATH.glob("*.npz"))
    return sorted(dirscan)


def generate_arguments(schema):
    """Function to generate arguments for DEEPaaS using schemas."""
    def arguments_function():  # fmt: skip
        logger.debug("Web args schema: %s", schema)
        return schema().fields
    return arguments_function


def predict_arguments(schema):
    """Decorator to inject schema as arguments to call predictions."""
    def inject_function_schema(func):  # fmt: skip
        get_args = generate_arguments(schema)
        sys.modules[func.__module__].get_predict_args = get_args
        return func  # Decorator that returns same function
    return inject_function_schema


def train_arguments(schema):
    """Decorator to inject schema as arguments to perform training."""
    def inject_function_schema(func):  # fmt: skip
        get_args = generate_arguments(schema)
        sys.modules[func.__module__].get_train_args = get_args
        return func  # Decorator that returns same function
    return inject_function_schema


def generate_callbacks(ckpt_name):
    """Generator for for training callbacks. It includes the generation
    of model checkpoints to be saved at the configured models path.

    Arguments:
        ckpt_name -- Models folder name for the ModelCheckpoint path.

    Returns:
        Tensorflow training callbacks list.
    """
    checkpoint_path = config.MODELS_PATH / ckpt_name
    return [callbacks.ModelCheckpoint(checkpoint_path, verbose=1)]
