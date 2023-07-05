"""Fixtures module for api metadata. This is a configuration file designed
to use prepare the test function arguments on the test_*.py files related
to this folder.

You can add new fixtures following the next structure:
```py
@pytest.fixture(scope="module", param=[{list of possible arguments}])
def argument_name(request):
    # You can add setup code here for your argument/fixture
    return request.param
```

A combination of all parameters will be used to run the tests. So be careful
when adding multiple parameters to the fixtures. For example the following
configuration will generate the following parameters which will be run on each
of the tests in this folder.
```py
@pytest.fixture(scope="module", param=[1,2])
...
@pytest.fixture(scope="module", param=['a','b'])
...
```
Parameters generated: [(1,'a'), (1,'b'), (2,'a'), (2,'b')]
"""
# pylint: disable=redefined-outer-name

import pytest
from deepaas.model.v2.wrapper import UploadedFile

import api


@pytest.fixture(scope="module", params=[])  # TODO: Add your checkpoints
def checkpoint(request):
    """Fixture to provide the checkpoint argument to api.predict."""
    return api.config.MODELS_PATH / request.param


@pytest.fixture(scope="module", params=[])  # TODO: Add your input files
def input_file(request):
    """Fixture to provide the input_file argument to api.predict."""
    return UploadedFile("", filename=api.config.DATA_PATH / request.param)


@pytest.fixture(scope="module", params=["application/json"])
def accept(request):
    """Fixture to provide the accept argument to api.predict."""
    return request.param


@pytest.fixture(scope="module", params=[None, 20])
def batch_size(request):
    """Fixture to provide the batch_size option to api.predict."""
    return request.param


@pytest.fixture(scope="module", params=[None, 2])
def steps(request):
    """Fixture to provide the steps option to api.predict."""
    return request.param


@pytest.fixture(scope="module")
def options(batch_size, steps):
    """Fixture to return arbitrary keyword options for predictions."""
    options = {}  # Customize/Complete with predict options
    options["batch_size"] = batch_size
    options["steps"] = steps
    return {k: v for k, v in options.items() if v is not None}


@pytest.fixture(scope="module")
def predictions(checkpoint, input_file, accept, options):
    """Fixture to return predictions to assert properties."""
    return api.predict(checkpoint, input_file, accept, **options)
