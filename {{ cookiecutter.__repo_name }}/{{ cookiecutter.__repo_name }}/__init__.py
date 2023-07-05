"""This model example to build feedforward neural network models from scratch
with Tensorflow and keras to recognize handwritten digit images.

The deep learning model — one of the most basic artificial neural networks
that resembles the original multi-layer perceptron — will learn to classify
digits from 0 to 9 from the MNIST dataset.

Based on the image inputs and their labels (supervised learning), the neural
network is trained to learn their features using forward propagation and
backpropagation (reverse-mode differentiation). The final output of the
network is a vector of 10 scores — one for each handwritten digit image. You
will also evaluate how good the model is at classifying the images on the
test set.

Based on "Deep learning on MNIST" at https://github.com/numpy/numpy-tutorials
and "Tensorflow tutorials" https://www.tensorflow.org/tutorials/keras.
"""
import numpy as np
import tensorflow as tf
from keras import layers

from {{ cookiecutter.__repo_name }} import config


def create_model(dropout_factor=0.5):
    """Creates a new MNIST model ready for training. The model is composed
    by multiple convolution layers with flatten and dropout before the last
    layer. It uses a `relu` activation function on the hidden layers.

    Keyword Arguments:
        dropout_factor -- Dropout after hidden layer (default: {0.5})

    Returns:
        Tensorflow MNIST model ready for training.
    """
    model = tf.keras.Sequential(
        [
            tf.keras.Input(shape=config.INPUT_SHAPE),
            layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
            layers.MaxPooling2D(pool_size=(2, 2)),
            layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
            layers.MaxPooling2D(pool_size=(2, 2)),
            layers.Flatten(),
            layers.Dropout(dropout_factor),
            layers.Dense(config.LABEL_DIMENSIONS, activation="softmax"),
        ]
    )
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
        loss=tf.keras.losses.CategoricalCrossentropy(from_logits=False),
        metrics=[tf.keras.metrics.CategoricalAccuracy()],
    )
    return model


def predict(model, input_data, **options):
    """Performs predictions on data using a MNIST model.

    Arguments:
        model -- Tensorflow/Keras model to use for predictions.
        input_data -- NPZ file with images equivalent to MNIST data.
        options -- See tensorflow/keras predict documentation.

    Returns:
        Return value from tf/keras model predict.
    """
    predict_data = np.load(input_data)
    return model.predict(predict_data, verbose="auto", **options)


def training(model, input_data, **options):
    """Performs training on a model from raw MNIST input and target data.

    Arguments:
        model -- Tensorflow/Keras model to train with data.
        input_data -- NPZ file with training images and labels.
        options -- See tensorflow/keras fit documentation.

    Returns:
        Return value from tf/keras model fit.
    """
    train_data = np.load(input_data).values()
    return model.fit(*train_data, verbose="auto", **options)
