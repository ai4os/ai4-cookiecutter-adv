"""Package to create dataset, build training and prediction pipelines
"""
# ! If you do not change names of functions, no need to modify this file !
#
# To publicly call mkdata(), predict(), and train() methods,
# we import them here:

# make dataset
from .dataset import mkdata as mkdata

# predict
from .models import predict as predict

# train
from .models import train as train

