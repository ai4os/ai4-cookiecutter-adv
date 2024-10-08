"""Pytest configuration file for cookiecutter-AI4EOSC project."""

# pylint: disable=redefined-outer-name
import os
import tempfile
from pathlib import Path

import pytest
import toml
import yaml
from cookiecutter.main import cookiecutter


@pytest.fixture(scope="session")
def cookiecutter_path():
    """Fixture to provide the cookiecutter path."""
    return Path(__file__).parents[1].resolve()


@pytest.fixture(scope="session", params=[])  # Define on tests
def config_file(request, cookiecutter_path):
    """Fixture to provide each cookiecutter configuration path."""
    return cookiecutter_path / f"tests/configurations/{request.param}.yml"


@pytest.fixture(scope="session")
def config_args(config_file):
    """Fixture to provide each cookiecutter configuration args."""
    with open(config_file, encoding="utf-8") as file:
        return yaml.load(file, Loader=yaml.FullLoader) or {}


@pytest.fixture(scope="session", name="testdir", autouse=True)
def create_testdir(config_file):
    """Fixture to generate a temporary directory for each config."""
    with tempfile.TemporaryDirectory() as testdir:
        os.chdir(testdir)
        yield testdir


@pytest.fixture(scope="session", name="project")
def bake_project(cookiecutter_path, testdir, config_args, project_name):
    """Fixture to bake a project from a cookiecutter template."""
    cookiecutter(
        template=str(cookiecutter_path),
        no_input=True,
        extra_context=config_args,
        output_dir="project",
    )
    project_dir = project_name.lower().replace(" ", "-")
    return Path(testdir) / "project" / project_dir


@pytest.fixture(scope="session")
def pyproject(project):
    """Fixture to provide parsed pyproject.toml."""
    with open(project / "pyproject.toml", encoding="utf-8") as file:
        return toml.load(file)


@pytest.fixture(scope="session")
def git_base_url(config_args):
    """Fixture to provide git_base_url."""
    default = "https://github.com/ai4os-hub"
    return config_args.get("git_base_url", default)


@pytest.fixture(scope="session")
def project_name(config_args):
    """Fixture to provide project_name."""
    return config_args.get("project_name", None)


@pytest.fixture(scope="session")
def repo_name(config_args, project_name):
    """Fixture to provide repo_name."""
    default = f"{project_name.lower().replace(' ', '-')}"
    return config_args.get("repo_name", default)


@pytest.fixture(scope="session")
def author_name(config_args):
    """Fixture to provide author_name."""
    return config_args.get("author_name", None)


@pytest.fixture(scope="session")
def author_email(config_args):
    """Fixture to provide author_email."""
    return config_args.get("author_email", None)


@pytest.fixture(scope="session")
def description(config_args):
    """Fixture to provide description."""
    return config_args.get("description", "")


@pytest.fixture(scope="session")
def app_version(config_args):
    """Fixture to provide app_version."""
    return config_args.get("app_version", "0.0.1")


@pytest.fixture(scope="session")
def open_source_license(config_args):
    """Fixture to provide open_source_license."""
    return config_args.get("open_source_license", "MIT")


@pytest.fixture(scope="session")
def dockerhub_user(config_args):
    """Fixture to provide dockerhub_user."""
    return config_args.get("dockerhub_user", "deephdc")


@pytest.fixture(scope="session")
def docker_baseimage(config_args):
    """Fixture to provide docker_baseimage."""
    return config_args.get("docker_baseimage", "tensorflow/tensorflow")


@pytest.fixture(scope="session")
def baseimage_cpu_tag(config_args):
    """Fixture to provide baseimage_cpu_tag."""
    return config_args.get("baseimage_cpu_tag", "2.9.1")


@pytest.fixture(scope="session")
def baseimage_gpu_tag(config_args):
    """Fixture to provide baseimage_gpu_tag."""
    return config_args.get("baseimage_gpu_tag", "2.9.1-gpu")


@pytest.fixture(scope="session")
def failure_notify(config_args):
    """Fixture to provide failure_notify."""
    return config_args.get("failure_notify", False)
