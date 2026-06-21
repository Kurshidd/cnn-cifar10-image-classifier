# 🧠 CNN CIFAR-10 Image Classifier

A Deep Learning Image Classification project built using **TensorFlow**, **Keras**, and **Streamlit**.

The model is trained on the CIFAR-10 dataset and can classify uploaded images into one of the following categories:

- ✈ Airplane
- 🚗 Automobile
- 🐦 Bird
- 🐱 Cat
- 🦌 Deer
- 🐶 Dog
- 🐸 Frog
- 🐴 Horse
- 🚢 Ship
- 🚚 Truck

---

# Project Demo

Upload an image through the Streamlit interface.

The application predicts

- Class Name
- Prediction Confidence

Example

Input Image

Dog

Prediction

Dog

Confidence

99.21%

---

# Features

- CNN Image Classification
- TensorFlow & Keras
- Streamlit Web Interface
- Upload Custom Images
- Confidence Score
- Clean Project Structure
- Easy Deployment

---

# Tech Stack

- Python
- TensorFlow
- Keras
- NumPy
- Pillow
- Streamlit
- Matplotlib

---

# Dataset

CIFAR-10

- 60,000 Images
- 10 Classes
- RGB Images
- 32 × 32 Resolution

---

# Project Structure

```text
CNN-CIFAR10-Image-Classifier

├── app.py

├── train.py

├── predict.py

├── requirements.txt

├── README.md

├── models

│      cnn_cifar10.keras

├── uploads

├── utils

│      preprocess.py

│      classes.py

└── screenshots
```

---

# Installation

Clone Repository

```bash
git clone https://github.com/yourusername/CNN-CIFAR10-Image-Classifier.git
```

Go to Project

```bash
cd CNN-CIFAR10-Image-Classifier
```

Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Install Packages

```bash
pip install -r requirements.txt
```

---

# Run Application

```bash
streamlit run app.py
```

---

# Model Training

Run

```bash
python train.py
```

The trained model will be saved inside

```
models/
```

---

# Prediction

Upload any supported image

Supported Formats

- JPG
- JPEG
- PNG

The model predicts the closest CIFAR-10 category.

---

# Future Improvements

- Transfer Learning
- EfficientNet
- MobileNet
- ResNet
- Real-time Webcam Prediction
- Docker Support
- Cloud Deployment
- Top-3 Predictions
- Model Explainability (Grad-CAM)

---

# Author

Khurshid Shaikh

---

# License

MIT License
