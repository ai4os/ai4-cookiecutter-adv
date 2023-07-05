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

import api


@pytest.fixture(scope="module", params=[])  # TODO: Add your checkpoints
def checkpoint(request):
    """Fixture to provide the checkpoint argument to api.train."""
    return api.config.MODELS_PATH / request.param


@pytest.fixture(scope="module", params=[])  # TODO: Add your datasets
def dataset(request):
    """Fixture to provide the dataset argument to api.train."""
    return api.config.DATA_PATH / request.param


@pytest.fixture(scope="module", params=[2])
def epochs(request):
    """Fixture to provide the epochs option to api.train."""
    return request.param


@pytest.fixture(scope="module", params=[None, 1])
def initial_epoch(request):
    """Fixture to provide the initial_epoch option to api.train."""
    return request.param


@pytest.fixture(scope="module", params=[None, False])
def shuffle(request):
    """Fixture to provide the shuffle option to api.train."""
    return request.param


@pytest.fixture(scope="module", params=[None, 0.1])
def validation_split(request):
    """Fixture to provide the validation_split option to api.train."""
    return request.param


@pytest.fixture(scope="module")
def options(epochs, initial_epoch, shuffle, validation_split):
    """Fixture to return arbitrary keyword arguments for training."""
    options = {}  # Customize/Complete with training options
    options["epochs"] = epochs
    options["initial_epoch"] = initial_epoch
    options["shuffle"] = shuffle
    options["validation_split"] = validation_split
    return {k: v for k, v in options.items() if v is not None}


@pytest.fixture(scope="module")
def training(checkpoint, dataset, options):
    """Fixture to perform and return training to assert properties."""
    return api.train(checkpoint, dataset, **options)
