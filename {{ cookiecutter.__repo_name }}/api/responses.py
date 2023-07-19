"""Module for defining custom API response parsers and content types.
"""
import logging
from . import config

logger = logging.getLogger(__name__)
logger.setLevel(config.log_level)

def json_response(values, **extra_values):
    """Converts the prediction or training results into json return format.

    Arguments:
        values -- Result value from method call.
        extra_values -- Not used, added for illustration purpose.

    Returns:
        Converted values into json dictionary format.
    """
    logger.debug("Response result: %d", values)
    logger.debug("Response options: %d", extra_values)
    return values.tolist()


def pdf_response(values, **extra_values):
    """Converts the prediction or training results into json return format.

    Arguments:
        values -- Result value from method call.
        extra_values -- Not used, added for illustration purpose.

    Returns:
        Converted values into pdf buffer format.
    """
    logger.debug("Response result: %d", values)
    logger.debug("Response options: %d", extra_values)
    raise NotImplementedError


content_types = {
    "application/json": json_response,
    "application/pdf": pdf_response,
}

