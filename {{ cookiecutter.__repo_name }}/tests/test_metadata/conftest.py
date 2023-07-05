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


@pytest.fixture(scope="module")
def metadata():
    """Fixture to return defined api metadata."""
    return api.get_metadata()
