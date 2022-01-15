import tensorflow as tf


def loadLiveness(path):
    model = tf.keras.models.load_model(path)
    return model
