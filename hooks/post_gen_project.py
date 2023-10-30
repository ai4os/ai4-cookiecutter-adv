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
import subprocess as subp
import sys


repo_name = "{{ cookiecutter.__repo_name }}"


def git_ini(repo):
    """Function to initialise git repositories"""
    gitrepo = os.path.join("{{ cookiecutter.git_base_url }}", repo + ".git")

    os.chdir(os.path.join("../", repo))
    subp.call(["git", "init"])
    subp.call(["git", "add", "."])
    subp.call(["git", "commit", "-m", "initial commit"])
    subp.call(["git", "remote", "add", "origin", gitrepo])

    # create test branch automatically
    subp.call(["git", "checkout", "-b", "test"])
    # adjust [Build Status] for the test branch
    readme_content = []
    with open("README.md") as f_old:
        for line in f_old:
            if "[![Build Status]" in line:
                line = line.replace("/main)", "/test)")
            readme_content.append(line)

    with open("README.md", "w") as f_new:
        for line in readme_content:
            f_new.write(line)

    subp.call(
        ["git", "commit", "-a", "-m", "update README.md for the BuildStatus"]
    )

    # switch back to master
    subp.call(["git", "checkout", "main"])

    return gitrepo


try:
    # initialized both git repositories
    git_user_app = git_ini(repo_name)
    message = f"""
------ SUCCESS ------
[Info] {repo_name} was created successfully,
       Don't forget to create corresponding remote repository: {git_user_app}
       then you can do 'git push origin --all'")
"""
    print(message)

except Exception as e:
    message = f"Something went wrong: {repr(e)}"
    print("[ERROR]: " + message)
    sys.exit(message)
