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

import requests
import requests.exceptions

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
FOLDER_REGEX = r"^[a-zA-Z0-9_-]+$"
MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
APP_VERSION_REGEX = r"^\d+\.\d+\.\d+$"
DOCKER_HUB_API = "https://registry.hub.docker.com/v2"
REQ_TIMEOUT = 1000  # Milliseconds


# -----------------------------------------------------------------------------
def validate_git_base_url():
    """Validate __git_base_url"""
    __git_base_url = urlparse(url="{{ cookiecutter.__git_base_url }}")
    if not bool(__git_base_url.scheme and __git_base_url.netloc):
        logging.error("Invalid __git_base_url %s", __git_base_url)
        raise ValueError("Invalid __git_base_url")


# -----------------------------------------------------------------------------
def validate_project_name():
    """Validate project_name"""
    project_name = "{{ cookiecutter.project_name }}"
    if len(project_name) < 2:
        logging.error("Invalid project name (%s), length < 2", project_name)
        raise ValueError("Invalid project name")
    if len(project_name.split(" ")) > 4:
        logging.error("Invalid project name (%s), words > 4", project_name)
        raise ValueError("Invalid project name")


def validate_repo_name():
    """Validate repo_name"""
    repo_name = "{{ cookiecutter.__repo_name }}"
    if not re.match(FOLDER_REGEX, repo_name):
        logging.error("Invalid characters in repo name (%s)", repo_name)
        raise ValueError("Invalid repository parsing")


def validate_app_name():
    """Validate app_name"""
    app_name = "{{ cookiecutter.__app_name }}"
    if not re.match(MODULE_REGEX, app_name):
        logging.error("Invalid package name (%s)", app_name)
        raise ValueError("Invalid package name parsing")


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
def validate_docker_image():
    """Validate docker image in docker hub"""
    # Construct the URL for Docker Hub API v2
    image = "{{ cookiecutter.docker_baseimage }}"
    cpu_tag = "{{ cookiecutter.baseimage_cpu_tag }}"
    gpu_tag = "{{ cookiecutter.baseimage_gpu_tag }}"

    if len("{{ cookiecutter.docker_baseimage }}".split("/")) > 2:
        return  # Skip validation for local or non-Docker Hub images

    cpu_image_url = f"{DOCKER_HUB_API}/repositories/{image}/tags/{cpu_tag}"
    try:
        response = requests.get(cpu_image_url, timeout=REQ_TIMEOUT)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        err_msg = f"Invalid docker image {image}:{cpu_tag}\n{err}"
        raise ValueError(err_msg) from err
    except requests.exceptions.Timeout:
        pass  # In case of network fail, continue

    gpu_image_url = f"{DOCKER_HUB_API}/repositories/{image}/tags/{gpu_tag}"
    try:
        response = requests.get(gpu_image_url, timeout=REQ_TIMEOUT)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        err_msg = f"Invalid docker image {image}:{cpu_tag}\n{err}"
        raise ValueError(err_msg) from err
    except requests.exceptions.Timeout:
        pass  # In case of network fail, continue


# -----------------------------------------------------------------------------
# If any of the validation, exit with error
try:
    validate_git_base_url()
    validate_project_name()
    validate_repo_name()
    validate_app_name()
    validate_authors()
    validate_app_version()
    validate_docker_image()
except ValueError as error:
    logging.error(error, exc_info=True)
    raise SystemExit(1) from error
