import streamlit as st
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np 
from nutrition import nutritional_info
from recpes import recipes
from food_facts import food_info_facts


def get_random_fact(food_class):
    facts = food_info_facts 
    return facts.get(food_class, 'Explore interesting facts about this food!')


def display_info(food_class, fact, nutritional_data):
    st.markdown(f"<h3 style='text-align: center;'>You are eating a {food_class.replace('_',' ')}! Cheers.</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>{fact}</p>", unsafe_allow_html=True)

    if nutritional_data:
        st.markdown("<h3 style='text-align: center;'>Nutritional Information</h2>", unsafe_allow_html=True)
        st.markdown(f"<p style = 'text-align: center;'>Calories: {nutritional_data.get('calories', 'N/A')} kcal</p>",unsafe_allow_html = True)
        st.markdown(f"<p style = 'text-align: center;'>Protein: {nutritional_data.get('protein', 'N/A')} g</p>",unsafe_allow_html = True)
        st.markdown(f"<p style = 'text-align: center;'>Carbs: {nutritional_data.get('carbs', 'N/A')} g</p>",unsafe_allow_html =True)
        st.markdown(f"<p style = 'text-align: center;'>Fat: {nutritional_data.get('fat', 'N/A')} g</p>",unsafe_allow_html=True)

def classify_food(uploaded_file, model , class_indices):
    img = load_img(uploaded_file, target_size = (224,224))
    img_array = img_to_array(img)
    img_array_inp = img_array.reshape(1, 224, 224, 3)
    final_img = img_array_inp/255.0
    soft_preds = model.predict(final_img)
    arg_ind = np.argmax(soft_preds)
    class_name = class_indices[arg_ind]
    fact = get_random_fact(class_name)
    nutritional_data = nutritional_info.get(class_name, {})
    display_info(class_name, fact, nutritional_data)
    recpe = recipes.get(class_name)
    st.markdown(f"<h3 style='text-align: center;'>Recipe for {class_name.replace('_',' ')}</h3>", unsafe_allow_html=True)
    st.image(img)
    st.write(f"\n{recpe}")
 


