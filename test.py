from ultralytics import YOLO
import cv2
import streamlit as st
from PIL import Image
import torch
import numpy as np
from class_labels_name import class_labels_names

# imgpath = r"C:\Users\LENOVO\Desktop\pro\img\val\1\82.jpg"
model = ROOT/'best.pt'
# img = cv2.imread(imgpath)
model = YOLO(modelpath)

st.title("HAPPY RAINNY KANOMTHAI..")
image = st.file_uploader("Choose .jpg pic ...", type=["png", "jpg", "jpeg"])
if image:
    image = Image.open(image)
    st.image(image=image)

    st.write("")
    st.write("Detecting...")

    result = model(image)
    names = result[0].names
    probability = result[0].probs.data.numpy()
    prediction = np.argmax(probability)
    className = int(names[prediction])
    className = class_labels_names[className]
    st.write(className)
