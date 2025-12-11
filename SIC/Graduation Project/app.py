import streamlit as st

st.set_page_config(page_title="Alzheimer’s MRI Classifier", layout="centered")

import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import preprocess_input as resnet_preprocess
from tensorflow.keras.models import load_model


IMG_SIZE = 224
CLASS_NAMES = ["Non Demented", "Very mild Dementia", "Mild Dementia"]


@st.cache_resource
def load_resnet_model():
    return load_model("final_resnet_3.keras")

model = load_resnet_model()


def preprocess_image(img_pil):
    img = img_pil.convert("RGB")
    img = img.resize((IMG_SIZE, IMG_SIZE))

    img_array = np.array(img).astype("float32")
    img_array = resnet_preprocess(img_array)
    img_array = np.expand_dims(img_array, axis=0)

    return img_array


def predict_image(img_pil):
    processed = preprocess_image(img_pil)
    preds = model.predict(processed)
    class_idx = np.argmax(preds)
    return CLASS_NAMES[class_idx], preds[0]


st.title("🧠 Alzheimer’s MRI Classification")
st.write(
    "Upload an MRI slice and click **Classify Image** to detect whether the patient is "
    "**Non Demented**, **Very Mild Dementia**, or **Mild Dementia**."
)

uploaded_file = st.file_uploader("Upload MRI Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded MRI Image", width=300)

    if st.button("🔍 Classify Image"):
        with st.spinner("Running prediction..."):
            label, probabilities = predict_image(img)

        prob_dict = {CLASS_NAMES[i]: float(probabilities[i]) for i in range(len(CLASS_NAMES))}

        st.success(f"### 🧾 Prediction: **{label}**")

        # st.write("### 📊 Class Probabilities")
        # st.json(prob_dict)

        # st.write("### 📈 Softmax Output")
        # st.bar_chart(probabilities)

else:
    st.info("Please upload an MRI image to begin.")
