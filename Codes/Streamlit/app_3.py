import streamlit as st
import requests
import io
from PIL import Image
import tempfile
import uuid

# Placeholder for your Hugging Face API setup
IMAGE_API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer <hf_token>"}

interior_styles = [
    'Indian', 'Minimal', 'Contemporary', 'Traditional', 'Art Deco', 'Scandinavian',
    'Industrial', 'Mid-Century Modern', 'Bohemian', 'Rustic', 'Shabby Chic', 'Hollywood Glam',
    'Coastal', 'French Country', 'Eclectic', 'Victorian', 'Baroque', 'Rococo', 'Gothic', 'Bauhaus',
    'Modern', 'Country', 'Zen', 'Retro', 'Mediterranean', 'Tropical', 'Asian', 'Craftsman', 'Farmhouse', 'Art Nouveau'
]

# Function to generate interior design images with slight prompt modifications
def generate_interior_design_images(description, num_images=4):
    images_paths = []
    for i in range(num_images):
        # Append a unique identifier to the prompt
        modified_description = f"{description} (variation {uuid.uuid4()})"
        payload = {"inputs": modified_description}
        response = requests.post(IMAGE_API_URL, headers=headers, json=payload)
        if response.ok:
            image_bytes = response.content
            image = Image.open(io.BytesIO(image_bytes))
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
                image.save(tmp_file.name, 'PNG')
                images_paths.append(tmp_file.name)
        else:
            st.error("Failed to generate images. Please check your input and try again.")
            break
    return images_paths

def main():
    st.title('DecorAIze: Your AI Interior Designer')
    
    room_type = st.selectbox('Choose a room to design:', ['Living Room', 'Bedroom', 'Kitchen', 'Bathroom', 'Dining Room'])
    style = st.selectbox('Choose your style:', ['', *interior_styles])
    objects_input = st.text_input('Enter or select objects to place in your room (comma separated):', help="Example: Sofa, Coffee Table")
    description = st.text_area('Additional details (e.g., colors, materials):')

    if st.button('Generate Interior Design'):
        full_description = f"{style} {room_type} with {objects_input}. {description}"
        image_paths = generate_interior_design_images(full_description)
        
        # Display images in a 2x2 grid
        if image_paths:
            cols = st.columns(2)  # Create two columns for the 2x2 grid
            for index, img_path in enumerate(image_paths):
                with cols[index % 2]:  # Alternate between columns
                    st.image(img_path, width=300, caption=f'Image {index + 1}')

if __name__ == "__main__":
    main()
