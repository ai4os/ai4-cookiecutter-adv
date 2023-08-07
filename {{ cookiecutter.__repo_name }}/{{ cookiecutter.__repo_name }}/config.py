"""Module to define CONSTANTS used across the AI-model package
"""
import logging
import os

# configure logging:
# logging level across various modules can be setup via USER_LOG_LEVEL,
# options: DEBUG, INFO(default), WARNING, ERROR, CRITICAL
ENV_LOG_LEVEL = os.getenv("USER_LOG_LEVEL", "INFO")
LOG_LEVEL = getattr(logging, ENV_LOG_LEVEL.upper())

# EXAMPLE on how to load environment variables
MY_PARAMETER_INT = int(os.getenv("MY_PARAMETER_INT", default="10"))
