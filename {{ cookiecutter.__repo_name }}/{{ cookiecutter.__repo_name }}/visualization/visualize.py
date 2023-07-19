"""Module for exploratory and results oriented visualizations
"""

import logging
import {{ cookiecutter.__repo_name }}.config as cfg

logger = logging.getLogger(__name__)
logger.setLevel(cfg.log_level)
