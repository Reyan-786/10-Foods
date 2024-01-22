# 10 Foods Streamlit App

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

3. Install dependencies:
      ```bash
      pip install -r requirements.txt
   ```

3. Run the app:
      ```bash
      streamlit run --server.runOnSave True app.py
   ```


## Usage
1. Open the app in your web browser.

2. Upload an image or capture one using the camera input.

3. Explore information about the identified food.

## File Structure

1. **app.py**: Main Streamlit app script.
2. **Models/preprocessed_mobileNet_3.h5**: Pre-trained deep learning model.
3. **utils.py**: Utility functions.
4. **nutrition.py**: Nutritional information data.
5. **recpes.py**: Recipes data.

**Visit the deployment** @ https://one0-foods-food-info-app.onrender.com/</h3>

<footer style='text-align: center;'>Crafted by Reyan.</footer>
