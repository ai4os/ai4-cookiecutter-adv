import pytest
import os


@pytest.mark.parametrize("config_file", ["config-1"], indirect=True)
def test_source_folder(project):
    raise NotImplementedError  # TODO: implement your test here


@pytest.mark.parametrize("config_file", ["config-1"], indirect=True)
def test_api_folder(project):
    assert os.path.exists(project / "api")
    assert os.path.exists(project / "api" / "__init__.py")
    assert os.path.exists(project / "api" / "config.py")
    assert os.path.exists(project / "api" / "responses.py")
    assert os.path.exists(project / "api" / "schemas.py")
    assert os.path.exists(project / "api" / "utils.py")


@pytest.mark.parametrize("config_file", ["config-1"], indirect=True)
def test_data_folder(project):
    assert os.path.exists(project / "data")
    assert os.path.exists(project / "data" / "external")
    assert os.path.exists(project / "data" / "processed")
    assert os.path.exists(project / "data" / "raw")


@pytest.mark.parametrize("config_file", ["config-1"], indirect=True)
def test_docker_folder(project):
    raise NotImplementedError  # TODO: implement your test here


@pytest.mark.parametrize("config_file", ["config-1"], indirect=True)
def test_docs_folder(project):
    assert os.path.exists(project / "docs")


@pytest.mark.parametrize("config_file", ["config-1"], indirect=True)
def test_models_folder(project):
    assert os.path.exists(project / "models")


@pytest.mark.parametrize("config_file", ["config-1"], indirect=True)
def test_notebooks_folder(project):
    assert os.path.exists(project / "notebooks")


@pytest.mark.parametrize("config_file", ["config-1"], indirect=True)
def test_references_folder(project):
    assert os.path.exists(project / "references")


@pytest.mark.parametrize("config_file", ["config-1"], indirect=True)
def test_reports_folder(project):
    assert os.path.exists(project / "reports")


@pytest.mark.parametrize("config_file", ["config-1"], indirect=True)
def test_tests_folder(project):
    assert os.path.exists(project / "tests")
    assert os.path.exists(project / "tests" / "configurations")
    assert os.path.exists(project / "tests" / "data")
    assert os.path.exists(project / "tests" / "models")
    assert os.path.exists(project / "tests" / "test_metadata")
    assert os.path.exists(project / "tests" / "test_predictions")
    assert os.path.exists(project / "tests" / "test_training")
    assert os.path.exists(project / "tests" / "conftest.py")
    assert os.path.exists(project / "tests" / "test_deepaas.py")
