import numpy as np
import keras
import tensorflow as tf
from keras.models import load_model
# from tf.keras.preprocessing import image
import os

class PredictPipeline:
    def __init__(self, filename) -> None:
        self.filname = filename
    
    
    def predict(self):
        
        model = load_model(os.path.join("artifacts","training", "model.h5"))
        image_name = self.filname
        test_image = tf.keras.preprocessing.image.load_img(image_name)
        test_image = tf.keras.preprocessing.image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)
        
        if result[0] == 1:
            prediction = "Healthy"
            return [{"image":prediction}]

        else:
            prediction = "Coccidiosis"
            return [{"image":prediction}]
        


