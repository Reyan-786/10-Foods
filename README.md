# 10Foods Streamlit App

## Overview

This Streamlit app, named 10Foods, allows users to upload or capture an image of food and identifies the food category using a pre-trained deep learning model.

## Features

- Image Classification: Upload or capture an image to get information about the food.
- Display Information: View the recognized food category, random facts, and nutritional information.
- Recipe Information: Explore a simple recipe associated with the identified food.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/10Foods-Streamlit-App.git
```
2. Install the requirements.txt
```bash
 pip install -r requirements.txt
```
3. Run the app.
   ```bash
   streamlit run --server.runOnSave True app.py
   ```

## Usage
1. Open the app in your web browser.

2. Upload an image or capture one using the camera input.

3. Explore information about the identified food.

## File Structure
-> app.py: Main Streamlit app script.
-> Models/preprocessed_mobileNet_3.h5: Pre-trained deep learning model.
-> utils.py: Utility functions.
-> nutrition.py: Nutritional information data.
-> recpes.py: Recipes data.

<h3>Visit the deployment @ https://one0-foods-food-info-app.onrender.com/</h3>

<footer> Crafted by Reyan.</footer>
