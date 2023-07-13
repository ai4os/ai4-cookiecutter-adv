"""Visualization
"""
# import package config.py
import {{ cookiecutter.__repo_name }}.config as cfg

logger = logging.getLogger(__name__)
log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_fmt)
