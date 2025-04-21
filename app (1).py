# pip install streamlit transformers torch pillow

import streamlit as st
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Title for the Streamlit app
st.title("🖼️ Image Description Generator")

# Upload image
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)

    # Display the image
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Initialize the BLIP processor and model
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    # Preprocess the image and generate caption
    inputs = processor(images=image, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)

    # Display the generated description
    st.subheader("Image Description:")
    st.write(caption)
