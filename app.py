import streamlit as st
from tensorflow.keras.models import load_model
from utils import classify_food

model = load_model('Models\\preprocessed_mobileNet_3.h5')

st.markdown("<h1 style='text-align: center; color: #FF5733;'>Hi Foody! 😋 </h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #333;'>Wanna know about the food that you are eating?</p>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #007BFF;'>Welcome to 10Foods app!</h3>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Want to upload a delicious photo?")

class_indices = {'chicken_curry': 0,
                 'chicken_wings': 1,
                 'fried_rice': 2,
                 'grilled_salmon': 3,
                 'hamburger': 4,
                 'ice_cream': 5,
                 'pizza': 6,
                 'ramen': 7,
                 'steak': 8,
                 'sushi': 9}

if uploaded_file is not None:
    classify_food(uploaded_file, model, class_indices)


st.markdown("<hr style='border: 1px solid #ddd;'>", unsafe_allow_html=True)


img_file_buffer = st.camera_input('eating a delicacy?')

if img_file_buffer is not None:
    classify_food(img_file_buffer, model, class_indices)

st.markdown("<footer style='text-align: center; color: #555; margin-top: 20px;'>Crafted by Reyan.</footer>", unsafe_allow_html=True)