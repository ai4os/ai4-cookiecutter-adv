#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 - 2023 Karlsruhe Institute of Technology - Steinbuch Centre for Computing
# This code is distributed under the MIT License
# Please, see the LICENSE file
# pylint: disable=missing-docstring,invalid-name
import logging
import re
from urllib.parse import urlparse

FOLDER_REGEX = r"^[a-zA-Z0-9_-]+$"
MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
APP_VERSION_REGEX = r"^\d+\.\d+\.\d+$"
error = False


# -----------------------------------------------------------------------------
def validate_git_base_url():
    """Validate git_base_url"""
    git_base_url = urlparse(url="{{ cookiecutter.git_base_url }}")
    if not bool(git_base_url.scheme and git_base_url.netloc):
        logging.error("Invalid git_base_url %s", git_base_url)
        raise ValueError("Invalid git_base_url")


# -----------------------------------------------------------------------------
def validate_model_name():
    """Validate model_name"""
    model_name = "{{ cookiecutter.model_name }}"
    if len(model_name) < 2:
        logging.error("Invalid project name (%s), length < 2", model_name)
        raise ValueError("Invalid project name")


def validate_model_slug():
    """Validate model_slug"""
    model_slug = "{{ cookiecutter.package_slug }}"
    if len(model_slug) < 2:
        logging.error("Invalid model slug (%s), length < 2", model_slug)
        raise ValueError("Invalid model slug")
    if not re.match(FOLDER_REGEX, model_slug):
        logging.error("Invalid characters in model slug (%s)", model_slug)
        raise ValueError("Invalid model slug")


def validate_package_name():
    """Validate package_name"""
    package_name = "{{ cookiecutter.package_name }}"
    if len(package_name) < 2:
        logging.error("Invalid package name (%s), length < 2", package_name)
        raise ValueError("Invalid package name")
    if not re.match(MODULE_REGEX, package_name):
        logging.error("Invalid package name (%s)", package_name)
        raise ValueError("Invalid package name")


# -----------------------------------------------------------------------------
def validate_authors():
    """Validate author_emails and author_names"""
    author_emails = "{{ cookiecutter.author_email }}".split(",")
    for email in author_emails:
        if not re.match(EMAIL_REGEX, email.strip()):
            logging.error("Invalid author_email %s", email)
            raise ValueError("Invalid author_email")
    author_names = "{{ cookiecutter.author_name }}".split(",")
    lens = n_authors, n_emails = len(author_names), len(author_emails)
    if n_emails != n_authors:
        logging.error("Authors (%s) not matching number of emails (%s)", *lens)
        raise ValueError("Authors not matching number of emails")


# -----------------------------------------------------------------------------
def validate_app_version():
    """Validate app_version"""
    app_version = "{{ cookiecutter.app_version }}"
    if not re.match(APP_VERSION_REGEX, app_version):
        logging.error("Invalid app_version %s", app_version)
        raise ValueError("Invalid app_version")


# -----------------------------------------------------------------------------
# If any of the validation checks failed, exit with error
try:
    validate_git_base_url()
    validate_model_name()
    validate_model_slug()
    validate_package_name()
    validate_authors()
    validate_app_version()
except ValueError as err:
    logging.error(err, exc_info=True)
    raise SystemExit(1) from err
