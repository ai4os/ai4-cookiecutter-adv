"""Testing module for api predictions. This is a test file designed to use
pytest and prepared for some basic assertions and to add your own tests.

You can add new tests following the next structure:
```py
def test_{description for the test}(prediction):
    assert {statement with prediction that returns true or false}
```

The conftest.py module in the same directory includes the fixture to return
to your tests inside the argument variable `predictions` the value generated
by your function defined at `api.predict`.

Here you can find some examples of tests:

# Tests that predictions are between 0 and 1.
def test_predictions_range(predictions):
    
    for prediction in predictions:
        assert all(0.0 <= x <= 1.1 for x in prediction)

# Tests that sum of ind predictions totals ~1.0.
def test_predictions_sum(predictions):  # TODO: FIx to your needs
    
    for prediction in predictions:
        assert 0.99 < sum(prediction) < 1.01

"""
# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument


def test_predictions_type(predictions):  # TODO: FIx to your needs
    """Tests that predictions is a dict type."""
    assert isinstance(predictions, dict)
