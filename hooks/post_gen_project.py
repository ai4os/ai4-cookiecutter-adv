#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 - 2019 Karlsruhe Institute of Technology - Steinbuch Centre for Computing
# This code is distributed under the MIT License
# Please, see the LICENSE file

""" 
    Post-hook script:
    1. Initialises git repositories
    2. Creates 'master', 'test' branches
    3. Switches back to 'master'
    
    NB: Check for the correct git_base_url (valid URL) and repo_name 
        happens in "pre_gen_project.py" hook!
"""

import os
import subprocess
import sys


def git_ini(project_name):
    """Function to initialise git repositories"""
    repo = os.path.join(
        "{{ cookiecutter.git_base_url }}", project_name + ".git"
    )

    os.chdir(os.path.join("../", project_name))
    subprocess.call(["git", "init"])
    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "commit", "-m", "initial commit"])
    subprocess.call(["git", "remote", "add", "origin", repo])

    # create test branch automatically
    subprocess.call(["git", "checkout", "-b", "test"])
    # adjust [Build Status] for the test branch
    readme_content = []
    with open("README.md", encoding="utf-8") as f_old:
        for line in f_old:
            if "[![Build Status]" in line:
                line = line.replace("/main)", "/test)")
            readme_content.append(line)

    with open("README.md", "w", encoding="utf-8") as f_new:
        for line in readme_content:
            f_new.write(line)

    subprocess.call(
        ["git", "commit", "-a", "-m", "update README.md for the BuildStatus"]
    )

    # switch back to master
    subprocess.call(["git", "checkout", "main"])
    return repo


try:
    # initialized both git repositories
    git_repo_url = git_ini("{{ cookiecutter.package_slug }}")
    message = f"""
------ SUCCESS ------
[Info] {{ cookiecutter.package_slug }} was created successfully,
       Don't forget to create corresponding remote repository: {git_repo_url}
       then you can do 'git push origin --all'")
"""
    print(message)

except subprocess.CalledProcessError as e:
    message = f"Something went wrong: {repr(e)}"
    message = f"Something went wrong: {repr(e)}"
    print("[ERROR]: " + message)
    sys.exit(message)
