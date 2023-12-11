import json

import pytest


@pytest.fixture(scope="session")
def metadata(project):
    """Fixture to provide parsed metadata.json."""
    with open(project / "metadata.json", encoding="utf-8") as file:
        return json.load(file)


@pytest.mark.parametrize("config_file", ["config-1", "config-2"], indirect=True)
def test_title(metadata, model_name):
    assert metadata["title"] == model_name


@pytest.mark.parametrize("config_file", ["config-1", "config-2"], indirect=True)
def test_summary(metadata, model_name):
    raise NotImplementedError  # TODO: implement your test here
