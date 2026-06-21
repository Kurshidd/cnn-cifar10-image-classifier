import tensorflow as tf
import numpy as np

from utils.classes import classes
from utils.preprocess import preprocess_image


model = tf.keras.models.load_model("models/cnn_cifar10.keras")


def predict(image):

    image = preprocess_image(image)

    prediction = model.predict(image)

    index = np.argmax(prediction)

    confidence = prediction[0][index]

    return classes[index], confidence