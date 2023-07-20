"""Utilities module for API endpoints and methods.
"""
import logging
import sys

from . import config

logger = logging.getLogger(__name__)
logger.setLevel(config.log_level)


def ls_dirs(path):
    """Utility to return a list of files available in `path` folder.
    Args:
        path: Directory path to scan
    Returns:
        A list of strings for found subdirectories.
    """
    logger.debug("Scanning at: %s", path)
    dirscan = (x.name for x in path.iterdir() if x.is_dir())
    return sorted(dirscan)


def ls_files(path, pattern):
    """Utility to return a list of files available in `path` folder.

    Args:
        path: Directory path to scan
        pattern: File pattern to filter found files. 
            See glob.glob() python function for possible patterns.
    Returns:
        A list of strings for files found according to the pattern.
    """
    logger.debug("Scanning at: %s", path)
    dirscan = (x.name for x in path.glob(pattern))
    return sorted(dirscan)


def copy_remote(frompath, topath):
    """Copy e.g. remote NextCloud folder in your local deployment or viceversa.

    Example:
        copy_remote('rshare:/data/images', '/srv/myapp/data/images')

    Args:
      frompath (str, pathlib.Path): Source folder to be copied
      topath (str, pathlib.Path): Destination folder
    """

    command = ["rclone", "copy", f"{frompath}", f"{topath}"]
    result = subprocess.Popen(command,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              text=True)
    output, error = result.communicate()
    if error:
        logger.error(f"Error while copying from/to remote directory: {error}")
    return output, error


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

