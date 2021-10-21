import tensorflow as tf
from tensorflow import keras
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ssl

(X_train, y_train), (X_test, y_test) = keras.datasets.cifar10.load_data()
