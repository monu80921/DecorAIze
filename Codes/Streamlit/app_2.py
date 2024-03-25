import streamlit as st
import requests
import io
from PIL import Image
import os

# Hugging Face API setup
IMAGE_API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}

# Define a more extensive list of interior design styles
interior_styles = [
    'Indian', 'Minimal', 'Contemporary', 'Traditional', 'Art Deco', 'Scandinavian',
    'Industrial', 'Mid-Century Modern', 'Bohemian', 'Rustic', 'Shabby Chic', 'Hollywood Glam',
    'Coastal', 'French Country', 'Eclectic', 'Victorian', 'Baroque', 'Rococo', 'Gothic', 'Bauhaus'
]

# Streamlit UI setup
st.title('DecorAIze: Your AI Interior Designer')

room_type = st.selectbox('Type of Room', ['Living Room', 'Bedroom', 'Kitchen', 'Bathroom', 'Dining Room'])
style = st.selectbox('Type of Style', interior_styles)
description = st.text_area('Description', 'Describe your dream interior in detail.')

# Function to generate interior design images
def generate_interior_design_images(description):
    payload = {"inputs": description}
    response = requests.post(IMAGE_API_URL, headers=headers, json=payload)
    if response.ok:
        image_bytes = response.content
        image = Image.open(io.BytesIO(image_bytes))
        image_path = "/content/generated_interior_design.png"
        image.save(image_path)
        return image_path
    else:
        return "Failed to generate images. Please check your input and try again."

if st.button('Generate Interior Design'):
    full_description = f"{room_type} in {style} style. {description}"
    image_path = generate_interior_design_images(full_description)
    if image_path.startswith("/content/"):
        st.image(image_path, caption='Your AI Generated Interior Design')
    else:
        st.error(image_path)
