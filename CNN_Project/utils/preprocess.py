from PIL import Image
import numpy as np


def preprocess_image(image):

    image = image.resize((32,32))

    image = np.array(image)

    image = image / 255.0

    image = np.expand_dims(image, axis=0)

    return image