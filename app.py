import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from utils import classify_food
from classes_of_food import class_name

tf.get_logger().setLevel('ERROR')

css = """
@keyframes pulse {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.1);
  }
  100% {
    transform: scale(1);
  }
}
"""

st.markdown(f'<style>{css}</style>',unsafe_allow_html =True)

model = load_model("Models/InceptionV3_Finetuned_loss7977_Acc_8248.h5")

st.markdown("<h1 style='text-align: center; color: #FF5733;'>Hi Foody! 🍓 </h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Wanna know about the food that you are eating?</p>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #007BFF; animation: pulse 2s infinite;'>Welcome to Food X Net!</h3>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Want to upload a delicious photo?")


if uploaded_file is not None:
    classify_food(uploaded_file, model, class_name)

st.markdown("<hr style='border: 1px solid #ddd;'>", unsafe_allow_html=True)

img_file_buffer = st.camera_input('eating a delicacy?')

if img_file_buffer is not None:
    classify_food(img_file_buffer, model, class_name)

st.markdown("<footer style='text-align: center; color: #555; margin-top: 20px;'>Crafted by Reyan.</footer>", unsafe_allow_html=True)