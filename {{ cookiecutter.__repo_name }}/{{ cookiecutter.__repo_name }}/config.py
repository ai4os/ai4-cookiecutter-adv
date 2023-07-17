"""Module to define CONSTANTS used across the AI-model package
"""
import logging
import os

# configure logging
log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_fmt)

# EXAMPLE on how to load environment variables
MY_PARAMETER_INT = int(os.getenv("MY_PARAMETER_INT", default="10"))
