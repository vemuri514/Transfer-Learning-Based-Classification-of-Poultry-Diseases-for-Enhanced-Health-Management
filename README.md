# 🐔 Transfer Learning-Based Classification of Poultry Diseases for Enhanced Health Management

This project leverages **transfer learning** with state-of-the-art CNN architectures (like VGG16, VGG19, ResNet50) to classify poultry diseases using image data. A user-friendly **Flask web interface** enables real-time disease prediction from uploaded images, aiming to support early detection and improved poultry farm management.

---

## 🧠 Motivation

Poultry farming plays a vital role in food security and rural economies. However, the outbreak of diseases can cause severe economic loss. Manual diagnosis is time-consuming and prone to error. This project aims to automate disease detection through AI, enabling fast, reliable, and accessible diagnostics for farmers and veterinarians.

---

## 🔍 Features

* ✅ Deep Learning with **Transfer Learning** (VGG16/VGG19/ResNet50)
* ✅ Image-based poultry disease classification
* ✅ Flask-based web application
* ✅ Easy-to-use UI for uploading and predicting disease from images
* ✅ Model accuracy reports and visualizations

---

## 📂 Project Structure

```
Transfer-Learning-Poultry-Disease/
│
├── model/
│   ├── vgg16_model.h5
│   ├── resnet50_model.h5
│   └── vgg19_model.h5
│
├── static/
│   └── uploads/                # Uploaded images
│
├── templates/
│   ├── index.html              # Main page
│   └── result.html             # Results display
│
├── app.py                      # Flask web app
├── preprocess.py               # Image preprocessing code
├── predict.py                  # Prediction helper functions
├── train_model.py              # Model training script
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

---

## ⚙️ Technologies Used

* Python 🐍
* TensorFlow / Keras
* Flask
* OpenCV / PIL
* HTML, CSS (basic for UI)

---

## 🛠️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/Transfer-Learning-Poultry-Disease.git
   cd Transfer-Learning-Poultry-Disease
   ```

2. **Create virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Download Trained Models**

   Place `.h5` model files inside the `model/` directory. If not available, you can train them using `train_model.py`.

---

## 🧪 Usage

1. **Start Flask app**

   ```bash
   python app.py
   ```

2. **Open your browser**
   Navigate to `http://127.0.0.1:5000/`

3. **Upload an image**

   * Choose a poultry image showing disease symptoms.
   * Click **Predict** to see the classification results.

---

## 🏷️ Supported Diseases (Example)

| Label ID | Disease Name      |
| -------- | ----------------- |
| 0        | Newcastle Disease |
| 1        | Avian Influenza   |
| 2        | Fowl Pox          |
| 3        | Healthy           |

*You can modify these labels in your code or dataset.*

---

## 📊 Model Performance (example)

| Model    | Accuracy | Loss |
| -------- | -------- | ---- |
| VGG16    | 92.3%    | 0.21 |
| ResNet50 | 90.1%    | 0.28 |
| VGG19    | 91.4%    | 0.24 |

---

## 📈 Sample Output

* Input Image: Uploaded by user
* Prediction: "Newcastle Disease"
* Confidence: 95.7%

---

## 📌 Future Work

* Add support for more diseases
* Deploy on cloud (AWS, GCP, or Heroku)
* Improve UI with Bootstrap
* Add multilingual support for rural areas


