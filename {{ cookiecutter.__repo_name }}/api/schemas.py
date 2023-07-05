"""Module for defining custom web fields to use on the API interface.
"""
import marshmallow
from webargs import ValidationError, fields, validate

from . import config, parsers, utils


class Checkpoint(fields.String):
    """Field that takes a string and validates against current available
    models at config.MODELS_PATH.
    """

    def _deserialize(self, value, attr, data, **kwargs):
        if value not in utils.ls_models():
            raise ValidationError(f"Checkpoint `{value}` not found.")
        return str(config.MODELS_PATH / value)


class Dataset(fields.String):
    """Field that takes a string and validates against current available
    data files at config.DATA_PATH.
    """

    def _deserialize(self, value, attr, data, **kwargs):
        if value not in utils.ls_datasets():
            raise ValidationError(f"Dataset `{value}` not found.")
        return str(config.DATA_PATH / value)


class PredArgsSchema(marshmallow.Schema):
    """Prediction arguments schema for api.predict function."""

    class Meta:  # Keep order of the parameters as they are defined.
        # pylint: disable=missing-class-docstring
        # pylint: disable=too-few-public-methods
        ordered = True

    checkpoint = Checkpoint(
        metadata={
            "description": "Checkpoint from metadata to use for predictions.",
        },
        required=True,
    )

    input_file = fields.Field(
        metadata={
            "description": "NPY file with images data for predictions.",
            "type": "file",
            "location": "form",
        },
        required=True,
    )

    batch_size = fields.Integer(
        metadata={
            "description": "Number of samples per batch.",
        },
        required=False,
        validate=validate.Range(min=1),
    )

    steps = fields.Integer(
        metadata={
            "description": "Steps before prediction round is finished.",
        },
        required=False,
        validate=validate.Range(min=1),
    )

    accept = fields.String(
        metadata={
            "description": "Return format for method response.",
            "location": "headers",
        },
        required=True,
        validate=validate.OneOf(parsers.content_types),
    )


class TrainArgsSchema(marshmallow.Schema):
    """Training arguments schema for api.train function."""

    class Meta:  # Keep order of the parameters as they are defined.
        # pylint: disable=missing-class-docstring
        # pylint: disable=too-few-public-methods
        ordered = True

    checkpoint = Checkpoint(
        metadata={
            "description": "Checkpoint from metadata to use for predictions.",
        },
        required=True,
    )

    dataset = Dataset(
        metadata={
            "description": "Dataset name from metadata for training input.",
        },
        required=True,
    )

    epochs = fields.Integer(
        metadata={
            "description": "Number of epochs to train the model.",
        },
        required=False,
        load_default=1,
        validate=validate.Range(min=1),
    )

    initial_epoch = fields.Integer(
        metadata={
            "description": "Epoch at which to start training.",
        },
        required=False,
        load_default=0,
        validate=validate.Range(min=0),
    )

    steps_per_epoch = fields.Integer(
        metadata={
            "description": "Steps before declaring an epoch finished.",
        },
        required=False,
        validate=validate.Range(min=0),
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
            "description": "Fraction of the data to be used as validation.",
        },
        required=False,
        load_default=0.0,
        validate=validate.Range(min=0.0, max=1.0),
    )

    validation_steps = fields.Integer(
        metadata={
            "description": "Steps to draw before stopping on validation.",
        },
        required=False,
        validate=validate.Range(min=0),
    )

    validation_batch_size = fields.Integer(
        metadata={
            "description": "Number of samples per validation batch.",
        },
        required=False,
        validate=validate.Range(min=0),
    )

    validation_freq = fields.Integer(
        metadata={
            "description": "Training epochs to run before validation.",
        },
        required=False,
        load_default=1,
        validate=validate.Range(min=1),
    )
