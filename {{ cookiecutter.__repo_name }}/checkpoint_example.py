"""Example module of how to create and train a model checkpoint.
"""
import time

import api
import {{ cookiecutter.__repo_name }} as ml_model

ckpt_name = f"{time.strftime('%Y%m%d-%H%M%S')}.cp.ckpt"
model = ml_model.create_model()

dataset = api.config.DATA_PATH / "train-dataset.npz"
options = {"batch_size": 128, "epochs": 15, "validation_split": 0.1}
options["callbacks"] = api.utils.generate_callbacks(ckpt_name)

ml_model.training(model, dataset, **options)
model.summary()
