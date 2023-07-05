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
"""
# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument


def test_predictions_type(predictions):
    """Tests that predictions is a list type."""
    assert isinstance(predictions, list)


def test_predictions_len(predictions):
    """Tests that predictions have length of 10."""
    for prediction in predictions[0:10]:
        assert isinstance(prediction, list)
        assert len(prediction) == 10


def test_predictions_range(predictions):
    """Tests that predictions are between 0 and 1."""
    for prediction in predictions[0:10]:
        assert all(0.0 <= x <= 1.1 for x in prediction)


def test_predictions_sum(predictions):
    """Tests that sum of ind predictions totals ~1.0."""
    for prediction in predictions[0:10]:
        assert 0.99 < sum(prediction) < 1.01
