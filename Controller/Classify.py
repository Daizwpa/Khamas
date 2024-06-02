import pandas as pd
import joblib
import os
import tensorflow as tf
import six
import numpy as np


class Classifier:

    def __init__(self, wieghts_path):
        assert os.path.exists(wieghts_path) == True
        self.model = model = tf.keras.models.load_model(wieghts_path)

    def Classify(self, image):
        # extract radimoic features
        image = np.expand_dims(image, axis=0)
        print(np.shape(image))
        result = self.model.predict(image)
        result = tf.squeeze(result).numpy()
        return result
