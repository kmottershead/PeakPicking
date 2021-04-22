import base64
import numpy as np
import io
from PIL import Image
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential, load_model
from keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array
from flask import request
from flask import jsonify
from flask import Flask

app = Flask(__name__)

def get_model():
    global model
    model = tf.keras.models.load_model('/models/MobileNetPTModel.h5')
    print(" * Model loaded!")
    
def preprocess_image(image, target_size):
    if image.mode != "RGB":
        image = image.convert("RGB")
    image_resize = image.resize(target_size)
    image_array = img_to_array(image_resize)
    image_expanded_dims = np.expand_dims(image_array, axis=0)
    return tf.keras.applications.mobilenet.preprocess_input(image_expanded_dims)


print(" * Loading Keras model...")
get_model()

@app.route("/predict", methods=["POST"])
def predict():
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    processed_image = preprocess_image(image, target_size=(224, 224))

    prediction = model.predict(processed_image).tolist()

    response = {
        'prediction': {
            'Peak': prediction[0][0],
            'No': prediction[0][1],
            'FI': prediction[0][2]
        }
    }
    return jsonify(response)