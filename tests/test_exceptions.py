import pytest
from pathlib import Path
from cookiecutter import main, exceptions


CONFIGURATIONS_PATH = Path(__file__).parents[0] / "configurations"
CONFIGURATIONS = set(["no-config"])


@pytest.mark.parametrize("config_file", CONFIGURATIONS, indirect=True)
def test_pre_gen_fails(cookiecutter_path, config_args):
    with pytest.raises(exceptions.FailedHookException) as excinfo:
        main.cookiecutter(
            template=str(cookiecutter_path),
            no_input=True,
            extra_context=config_args,
            output_dir="project",
        )
    assert "Hook script failed" in str(excinfo.value)
