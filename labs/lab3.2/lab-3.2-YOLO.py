"""
references:

https://docs.streamlit.io/library/api-reference/media/st.image
"""

import torch
import streamlit as st
from PIL import Image
import numpy as np


st.title("YOLO Example")
st.text("Basic user driven YOLO object detection example")

st.header("Upload an image:")
uploaded_file = st.file_uploader("upload an image file for object detection", type=['png', 'jpg', 'jpeg'])

st.header("Image input:")
if uploaded_file is not None:
    # To read file as bytes:
    img = Image.open(uploaded_file)
    img_array = np.array(img)
    
    # Show the image filename and image.
    st.write(f'file: {uploaded_file}')
    st.write(type(uploaded_file))
    st.write(f'X: {img_array.shape}')
    st.image(img)

    st.header("Object Detection:")
    st.subheader("Results")

    # Model
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

    # Inference
    results = model(img)

    # Results
    results.print()
    results.save()  # or .save()
    
    classified_img = Image.open('./runs/detect/exp/image0.jpg')
    st.image(classified_img)

    results.pandas().xyxy[0]  # img1 predictions (pandas)
