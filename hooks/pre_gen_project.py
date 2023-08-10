#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 - 2023 Karlsruhe Institute of Technology - Steinbuch Centre for Computing
# This code is distributed under the MIT License
# Please, see the LICENSE file
# pylint: disable=missing-docstring,invalid-name
import re
from urllib.parse import urlparse

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
APP_VERSION_REGEX = r"^\d+\.\d+\.\d+$"
error = False


# Validate git_base_url
git_base_url = "{{ cookiecutter.git_base_url}}"
git_base_url = urlparse(url=git_base_url)
if not bool(git_base_url.scheme and git_base_url.netloc):
    print("[ERROR]:", f"Invalid git_base_url {git_base_url}")
    error = True


# Validate author_emails
author_emails = "{{ cookiecutter.author_email}}".split(",")
for email in author_emails:
    if not re.match(EMAIL_REGEX, email.strip()):
        print("[ERROR]:", f"Invalid author_email {email}")
        error = True


# Validate length of author_emails
author_names = "{{ cookiecutter.author_name}}".split(",")
n_authors, n_emails = len(author_names), len(author_emails)
if n_emails != n_authors:
    error_msg = "Authors ({}) not matching number of emails ({})"
    print("[ERROR]:", error_msg.format(n_authors, n_emails))
    error = True


# Validate app_version
app_version = "{{ cookiecutter.app_version}}"
if not re.match(APP_VERSION_REGEX, app_version):
    print("[ERROR]:", f"Invalid app_version {app_version}")
    error = True


# Validate repo_name
project_name = "{{ cookiecutter.project_name}}"
repo_name = "{{ cookiecutter.__repo_name}}"
if not re.match(MODULE_REGEX, repo_name) or len(repo_name) < 2:
    error_msg = "Invalid project name ({}), parsed as: ({})"
    print("[ERROR]:", error_msg.format(project_name, repo_name))
    error = True


# If any of the validation checks failed, exit with error
if error:
    raise SystemExit(1)
