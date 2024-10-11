import streamlit as st
from PIL import Image
import numpy as np
import cv2
import time

def add_custom_css():
    st.markdown("""
    <style>
    /* Professional gradient background */
    .stApp {
        background: linear-gradient(135deg, #1c2841, #2c3e50);
        color: #fff;
        font-family: 'Arial', sans-serif;
    }

    /* Main container */
    .main-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem;
        position: relative;
        z-index: 1;
    }

    /* Team Fin Heading */
    h1 {
        color: #3498db;
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-top: 0;
        margin-bottom: 0.5rem;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    /* Forgery Detection Heading */
    h2 {
        color: #e74c3c;
        font-size: 2rem;
        font-weight: bold;
        text-align: center;
        margin-top: 0;
        margin-bottom: 1rem;
        letter-spacing: 0.5px;
    }

    /* File upload area */
    .css-1cpxqw2 {
        background: rgba(255, 255, 255, 0.1);
        border: 2px solid #3498db;
        color: #fff;
        border-radius: 8px;
        transition: all 0.3s ease;
        text-align: center;
        margin-bottom: 1rem;
    }

    .css-1cpxqw2:hover {
        background: rgba(52, 152, 219, 0.2);
    }

    /* Download button */
    .stButton button {
        background-color: #2ecc71;
        color: white;
        font-size: 1.2rem;
        border-radius: 6px;
        padding: 0.7rem 1.4rem;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .stButton button:hover {
        background-color: #27ae60;
    }

    /* Logos container */
    .logo-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        margin-bottom: 1rem;
    }

    .logo {
        height: 40px;
        transition: transform 0.3s ease-in-out;
    }

    .logo:hover {
        transform: scale(1.1);
    }

    /* Background detective */
    .background-detective {
        position: fixed;
        top: 0;
        right: 0;
        height: 100vh;
        opacity: 0.1;
        z-index: 0;
        pointer-events: none;
    }

    /* Forgery icons */
    .forgery-icons {
        display: flex;
        justify-content: space-around;
        margin: 2rem 0;
    }

    .forgery-icon {
        width: 80px;
        height: 80px;
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 2rem;
    }

    /* Info boxes */
    .info-boxes {
        display: flex;
        justify-content: space-between;
        margin: 2rem 0;
    }

    .info-box {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 1rem;
        width: 30%;
        text-align: center;
    }

    .info-box h3 {
        color: #3498db;
        margin-bottom: 0.5rem;
    }

    /* Image comparison container */
    .image-comparison {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: 2rem 0;
    }

    .image-container {
        width: 45%;
        text-align: center;
    }

    .image-container img {
        max-width: 100%;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
    }

    .vs-icon {
        font-size: 2rem;
        color: #e74c3c;
    }
    </style>
    """, unsafe_allow_html=True)

def display_logos():
    st.markdown("""
    <div class="logo-container">
        <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" class="logo" alt="Python">
        <img src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png" class="logo" alt="Streamlit">
        <img src="https://upload.wikimedia.org/wikipedia/commons/3/31/NumPy_logo_2020.svg" class="logo" alt="NumPy">
        <img src="https://upload.wikimedia.org/wikipedia/commons/e/ed/Pandas_logo.svg" class="logo" alt="Pandas">
        <img src="https://upload.wikimedia.org/wikipedia/commons/1/10/PyTorch_logo_icon.svg" class="logo" alt="PyTorch">
    </div>
    """, unsafe_allow_html=True)

def add_background_detective():
    st.markdown("""
    <img src="/api/placeholder/400/800" class="background-detective" alt="Detective silhouette">
    """, unsafe_allow_html=True)

def add_forgery_icons():
    st.markdown("""
    <div class="forgery-icons">
        <div class="forgery-icon">🔍</div>
        <div class="forgery-icon">🖼️</div>
        <div class="forgery-icon">🔒</div>
        <div class="forgery-icon">📊</div>
    </div>
    """, unsafe_allow_html=True)

def add_info_boxes():
    st.markdown("""
    <div class="info-boxes">
        <div class="info-box">
            <h3>Image Analysis</h3>
            <p>Our advanced algorithms analyze pixel patterns and metadata to detect inconsistencies.</p>
        </div>
        <div class="info-box">
            <h3>AI-Powered</h3>
            <p>State-of-the-art machine learning models trained on vast datasets of authentic and forged images.</p>
        </div>
        <div class="info-box">
            <h3>Quick Results</h3>
            <p>Get instant feedback on potential forgeries with our real-time processing system.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def add_image_comparison():
    st.markdown("""
    <div class="image-comparison">
        <div class="image-container">
            <img src="/api/placeholder/400/300" alt="Original Image">
            <p>Original Image</p>
        </div>
        <div class="vs-icon">VS</div>
        <div class="image-container">
            <img src="/api/placeholder/400/300" alt="Forged Image">
            <p>Potential Forgery</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def load_model():
    with st.spinner("Initializing model..."):
        time.sleep(2)
    return "Loaded Model"

def process_image_with_model(image, model):
    processed_image = cv2.GaussianBlur(image, (15, 15), 0)
    return processed_image

add_custom_css()
add_background_detective()

st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Move headings to the top
st.markdown("<h1>Team Fin</h1>", unsafe_allow_html=True)
st.markdown("<h2>Forgery Detection</h2>", unsafe_allow_html=True)

# Display logos
display_logos()

# File upload
uploaded_file = st.file_uploader("Upload an image for forgery detection", type=["jpg", "jpeg", "png"])

add_forgery_icons()

st.write("Welcome to our state-of-the-art Forgery Detection system. Upload an image to check for potential manipulations.")

add_info_boxes()

add_image_comparison()

model = load_model()

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    image_np = np.array(image)

    if len(image_np.shape) == 3 and image_np.shape[2] == 3:
        image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    with st.spinner("Analyzing for potential forgery..."):
        processed_image = process_image_with_model(image_np, model)

    processed_image_rgb = cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB)

    st.image(processed_image_rgb, caption="Analyzed Image", use_column_width=True)

    st.download_button("Download Analyzed Image", data=Image.fromarray(processed_image_rgb).tobytes(), file_name="analyzed_image.png", mime="image/png")

st.markdown('</div>', unsafe_allow_html=True)