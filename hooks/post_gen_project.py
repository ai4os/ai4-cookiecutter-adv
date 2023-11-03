#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 - 2019 Karlsruhe Institute of Technology - Steinbuch Centre for Computing
# This code is distributed under the MIT License
# Please, see the LICENSE file
import contextlib
import logging
import os
import shutil
import subprocess
from pathlib import Path


# -----------------------------------------------------------------------------
# Use contextlib.chdir when python.version >= 3.11
@contextlib.contextmanager
def context_chdir(target_dir):
    original_directory = os.getcwd()
    os.chdir(target_dir)
    try:
        yield
    finally:
        os.chdir(original_directory)


# -----------------------------------------------------------------------------
def adjust_readme(branch):
    """Function to adjust README.md"""
    # adjust [Build Status] for the test branch
    readme_content = []
    with open("README.md", encoding="utf-8") as f_old:
        for line in f_old:
            if "[![Build Status]" in line:
                line = line.replace("/main)", f"/{branch})")
            readme_content.append(line)

    # write changes to README.md
    with open("README.md", "w", encoding="utf-8") as f_new:
        for line in readme_content:
            f_new.write(line)


# -----------------------------------------------------------------------------
def git_init(base_url, project_name):
    """Function to initialise git repositories"""
    repo = f"{base_url}/{project_name}.git"
    with context_chdir(Path(f"../{project_name}")):
        subprocess.call(["git", "init"])
        subprocess.call(["git", "add", "."])
        subprocess.call(["git", "commit", "-m", "initial commit"])
        subprocess.call(["git", "remote", "add", "origin", repo])
    return repo


def create_branch(project_name, branch):
    """Function to create branches"""
    with context_chdir(Path(f"../{project_name}")):
        # create test branch automatically
        subprocess.call(["git", "checkout", "-b", branch])

        # adjust README.md
        adjust_readme(branch)

        # commit changes
        commit_msg = "update README.md for the BuildStatus"
        subprocess.call(["git", "commit", "-a", "-m", commit_msg])

        # switch back to master
        subprocess.call(["git", "checkout", "main"])


# -----------------------------------------------------------------------------
# Run post generation actions, exit with error
try:
    # remove model source if not needed
    if "{{ cookiecutter.add_model_source }}" == False:
        shutil.rmtree("{{ cookiecutter.__model_source }}")

    # Initialise git repository and create test and dev branches
    git_repo_url = git_init(
        "{{ cookiecutter.git_base_url }}", "{{ cookiecutter.package_slug }}"
    )
    create_branch("{{ cookiecutter.package_slug }}", branch="test")
    create_branch("{{ cookiecutter.package_slug }}", branch="dev")

    # Log success information
    logging.info("Project {{ cookiecutter.package_slug }} created successfully")
    logging.info("Don't forget to create the remote repo: %s", git_repo_url)


except subprocess.CalledProcessError as err:
    logging.error(err, exc_info=True)
    raise SystemExit(1) from err
