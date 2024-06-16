import pickle
from PIL import Image
from io import BytesIO
from img2vec_pytorch import Img2Vec
import streamlit as st
import torch
from torchvision import transforms

# Load the pickled model
with open('pages/model_lions_cheetahs.p', 'rb') as f:
    model = pickle.load(f)

img2vec = Img2Vec()

# Streamlit Web App Interface
st.set_page_config(layout="wide", page_title="Image Classification for Lions And Cheetahs")

st.write("## Image Classification Demo")
st.write("Upload an image to predict whether it's a Lion or Cheetah.")

# Function to convert image to bytes
@st.cache
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="JPEG")
    byte_im = buf.getvalue()
    return byte_im

# Function to process uploaded image and display prediction
def fix_image(upload):
    image = Image.open(upload).convert('RGB')  # Ensure image is in RGB format
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    # Perform image vectorization
    features = img2vec.get_vec(image)

    # Predict using the loaded model
    prediction = model.predict([features])[0]

    # Display prediction
    st.write(f'Description: {prediction}')

# Interface layout
col1, col2 = st.columns(2)
uploaded_file = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Check file size
    if uploaded_file.size > 5 * 1024 * 1024:
        st.sidebar.error("File size exceeded maximum limit (5MB).")
    else:
        fix_image(uploaded_file)
else:
    st.sidebar.info('Please upload an image.')


