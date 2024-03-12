import streamlit as st
import requests
from PIL import Image
from io import BytesIO

API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
API_KEY = "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"

def generate_image(prompt):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        # Convert the response content into an image
        image = Image.open(BytesIO(response.content))
        return image
    else:
        return None

st.title('Image Generator with Hugging Face')

prompt = st.text_input("Enter a prompt for the image you want to generate:")

if st.button('Generate'):
    if prompt:
        result = generate_image(prompt)
        if result:
            st.image(result, caption="Generated Image")
        else:
            st.error("Error generating image. Please check the prompt or try again later.")
    else:
        st.error("Please enter a prompt.")
