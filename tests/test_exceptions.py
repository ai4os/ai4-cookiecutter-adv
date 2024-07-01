from pathlib import Path

import pytest
from cookiecutter.exceptions import FailedHookException
from cookiecutter.main import cookiecutter

CONFIGURATIONS_PATH = Path(__file__).parents[0] / "configurations"
CONFIGURATIONS = set(["no-config"])


@pytest.mark.parametrize("config_file", CONFIGURATIONS, indirect=True)
def test_pre_gen_fails(cookiecutter_path, config_args):
    with pytest.raises(FailedHookException) as excinfo:
        cookiecutter(
            template=str(cookiecutter_path),
            no_input=True,
            extra_context=config_args,
            output_dir="project",
        )
    assert "Hook script failed" in str(excinfo.value)


@pytest.mark.parametrize("config_file", ["bad-name"], indirect=True)
def test_bad_name(cookiecutter_path, config_args):
    with pytest.raises(FailedHookException) as excinfo:
        cookiecutter(
            template=str(cookiecutter_path),
            no_input=True,
            extra_context=config_args,
            output_dir="project",
        )
    assert "Hook script failed" in str(excinfo.value)


@pytest.mark.parametrize("config_file", ["bad-submodule"], indirect=True)
def test_bad_submodule(cookiecutter_path, config_args):
    with pytest.raises(FailedHookException) as excinfo:
        cookiecutter(
            template=str(cookiecutter_path),
            no_input=True,
            extra_context=config_args,
            output_dir="project",
        )
    assert "Hook script failed" in str(excinfo.value)
