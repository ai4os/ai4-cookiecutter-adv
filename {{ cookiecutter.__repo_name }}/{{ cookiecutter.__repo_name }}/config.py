"""Module to define CONSTANTS used across the AI-model package
"""
import logging
import os

# configure logging:
# logging level accross various modules can be setup via USER_LOG_LEVEL, 
# options: DEBUG, INFO(default), WARNING, ERROR, CRITICAL
env_log_level = os.getenv('USER_LOG_LEVEL', 'INFO')
log_level = getattr(logging, env_log_level.upper())
# logging format:
log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=log_fmt)

# EXAMPLE on how to load environment variables
MY_PARAMETER_INT = int(os.getenv("MY_PARAMETER_INT", default="10"))
