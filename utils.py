import streamlit as st
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np 
from nutrition import nutritional_info
from recpes import recipes


def get_random_fact(food_class):
    facts = {
    'chicken_curry': 'Did you know that chicken curry is a staple in many Asian cuisines?',
    'chicken_wings': 'Chicken wings are believed to have originated in Buffalo, New York, in the 1960s.',
    'fried_rice': 'Fried rice is a popular dish in Chinese cuisine and can be traced back to the Sui Dynasty.',
    'grilled_salmon': 'Salmon is rich in omega-3 fatty acids, which are good for heart health.',
    'hamburger': 'The hamburger is a classic American dish and has a disputed origin between various U.S. cities.',
    'ice_cream': 'The world\'s largest ice cream cone, made in Norway, measured over 3 meters tall!',
    'pizza': 'Pizza has its roots in Italy and has become a global favorite with countless variations.',
    'ramen': 'Ramen is a Japanese dish that consists of Chinese-style wheat noodles served in a meat or fish-based broth.',
    'steak': 'A perfectly cooked steak is a culinary delight, with preferences ranging from rare to well-done.',
    'sushi': 'Sushi is a traditional Japanese dish that typically consists of vinegared rice and various ingredients like seafood and vegetables.'
    }
    return facts.get(food_class, 'Explore interesting facts about this food!')

def display_info(food_class, fact, nutritional_data):
    st.markdown(f"<h3 style='text-align: center;'>You are eating a {food_class}! Cheers.</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>{fact}</p>", unsafe_allow_html=True)

    if nutritional_data:
        st.markdown("<h2 style='text-align: center;'>Nutritional Information</h2>", unsafe_allow_html=True)
        st.write(f"Calories: {nutritional_data.get('calories', 'N/A')} kcal")
        st.write(f"Protein: {nutritional_data.get('protein', 'N/A')} g")
        st.write(f"Carbs: {nutritional_data.get('carbs', 'N/A')} g")
        st.write(f"Fat: {nutritional_data.get('fat', 'N/A')} g")

def classify_food(uploaded_file, model , class_indices):
    img = load_img(uploaded_file, target_size = (224,224))
    img_array = img_to_array(img)
    img_array_inp = img_array.reshape(1, 224, 224, 3)
    final_img = img_array_inp/255.0
    soft_preds = model.predict(final_img)
    arg_ind = np.argmax(soft_preds)
    class_name = list(class_indices.keys())[arg_ind]
    fact = get_random_fact(class_name)
    nutritional_data = nutritional_info.get(class_name, {})
    display_info(class_name, fact, nutritional_data)
    recpe = recipes.get(class_name)
    st.markdown(f"<h3 style='color: #333; text-align: center;'>Recipe for {class_name}</h3>", unsafe_allow_html=True)
    st.image(img)
    st.write(f"\n{recpe}")
 

