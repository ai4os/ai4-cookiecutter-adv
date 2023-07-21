"""Module for defining custom web fields to use on the API interface.
"""
import marshmallow
from webargs import ValidationError, fields, validate

from . import config, responses, utils


class Checkpoint(fields.String):
    """Field that takes a string and validates against current available
    models at config.MODELS_PATH.
    """

    def _deserialize(self, value, attr, data, **kwargs):
        if value not in utils.ls_dir(config.MODELS_PATH):
            raise ValidationError(f"Checkpoint `{value}` not found.")
        return str(config.MODELS_PATH / value)


# EXAMPLE of Prediction Args description
# = HAVE TO MODIFY FOR YOUR NEEDS =
class PredArgsSchema(marshmallow.Schema):
    """Prediction arguments schema for api.predict function."""

    class Meta:  # Keep order of the parameters as they are defined.
        # pylint: disable=missing-class-docstring
        # pylint: disable=too-few-public-methods
        ordered = True

    checkpoint = Checkpoint(
        metadata={
            "description": "Checkpoint to use for predictions (Check metadata for the list of available checkpoints).",
        },
        required=False,
    )

    input_file = fields.Field(
        metadata={
            "description": "Data file to execute prediction on.",
            "type": "file",
            "location": "form",
        },
        required=True,
    )

    accept = fields.String(
        metadata={
            "description": "Return format for the response.",
            "location": "headers",
        },
        required=True,
        validate=validate.OneOf(list(responses.content_types)),
    )

# EXAMPLE of Training Args description
# = HAVE TO MODIFY FOR YOUR NEEDS =
class TrainArgsSchema(marshmallow.Schema):
    """Training arguments schema for api.train function."""

    class Meta:  # Keep order of the parameters as they are defined.
        # pylint: disable=missing-class-docstring
        # pylint: disable=too-few-public-methods
        ordered = True


    dataset = fields.String(
        metadata={
            "description": "Path to the training dataset.",
        },
        required=False,
    )

    batch_size = fields.Integer(
        metadata={
            "description": "Number of samples per batch.",
        },
        required=False,
        load_default=8,
        validate=validate.Range(min=0),
    )

    epochs = fields.Integer(
        metadata={
            "description": "Number of epochs to train the model.",
        },
        required=False,
        load_default=1,
        validate=validate.Range(min=1),
    )

    shuffle = fields.Boolean(
        metadata={
            "description": "Shuffle the training data before each epoch.",
        },
        required=False,
        load_default=True,
    )

    validation_split = fields.Float(
        metadata={
            "description": "Fraction of the data to be used for validation (0 .. 1).",
        },
        required=False,
        load_default=0.1,
        validate=validate.Range(min=0.0, max=1.0),
    )

    validation_freq = fields.Integer(
        metadata={
            "description": "Training epochs to run before validation.",
        },
        required=False,
        load_default=1,
        validate=validate.Range(min=1),
    )
