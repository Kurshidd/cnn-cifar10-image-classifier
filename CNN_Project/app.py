import streamlit as st
from PIL import Image

from predict import predict

st.set_page_config(
    page_title="CNN Image Classifier",
    page_icon="🧠",
    layout="centered"
)

st.title("CNN Image Classifier")

st.write("Upload an image.")

uploaded_file = st.file_uploader(
    "Choose Image",
    type=["jpg","jpeg","png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(image, width=300)

    if st.button("Predict"):

        label, confidence = predict(image)

        st.success(f"Prediction : {label}")

        st.write(f"Confidence : {confidence*100:.2f}%")