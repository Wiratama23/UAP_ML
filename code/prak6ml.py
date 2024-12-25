from pathlib import Path
import streamlit as st
import numpy as np
import tensorflow as tf

# Title and subtitle for the app
st.title("Romadhon Wiratama")
st.subheader("202110370311471")

# File uploader for image input
upload = st.file_uploader("Upload for prediction", type=["png", "jpg", "jpeg"])

# Dropdown for model selection
model_name = st.selectbox("Choose the model to use", ["mobilenetv2", "inceptionv3"])

# Define the prediction function
def predict(upload, model_name):
    result = ""
    confidence = 0
    img = tf.keras.utils.load_img(upload, target_size=(150, 150, 3))
    img_array = np.array(img) / 255.0 
    img_array = np.expand_dims(img_array, axis=0)
    
    # Load the pre-trained model
    model = tf.keras.models.load_model(Path(__file__).parent / f"../model/crack_{model_name}.h5")
    
    # Get predictions
    predictions = model.predict(img_array)  
    if predictions[0][0] <= 0.5:
        result = "No Crack"
        confidence = (1 - predictions[0][0]) * 100
    else:
        result = "Crack"
        confidence = predictions[0][0] * 100
    return result, confidence

# Prediction button
if st.button("Predict", type="primary"):
    if upload is not None:
        st.image(upload, caption="Uploaded Image", use_column_width=True)
        st.subheader("Prediction Results:")
        with st.spinner("Processing the image for prediction..."):
            try:
                result, confidence = predict(upload, model_name)
                st.write(f"Predicted Class: **{result}**")
                st.write(f"Confidence: **{confidence:.2f}%**")
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please upload an image before clicking Predict!")
