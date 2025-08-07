from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# Load the trained model
model = load_model("healthy_vs_rotten.h5")

# Class names
class_names = ['Coccidiosis', 'Healthy', 'NewCastle', 'Salmonella']

# Prediction function
def predict_disease(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]
    return predicted_class

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filepath = os.path.join('static', file.filename)
            file.save(filepath)
            prediction = predict_disease(filepath)
            return render_template('index.html', prediction=prediction, image_path=filepath)
    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
