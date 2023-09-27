
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import tensorflow as tf
import keras
from keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array

st.title('Villian image classification')




#load deep learning model
loaded_model = load_model(r'/content/villian_image_classification_VGG16.h5')

class_names = ['Darth Vader', 'Green Goblin', 'Joker', 'Thanos', 'Venom']


def predict_image(image):
  img = load_img(image, target_size = (224, 224))
  img_array = img_to_array(img)
  img_array = img_array/255
  img_array = np.expand_dims(img_array, axis = 0)

  classes = loaded_model.predict([img_array])
  class_index = np.argmax(classes, axis = 1)[0]
  class_name = class_names[class_index]
  confidence = round(100*np.max(classes), 2)

  im = mpimg.imread(image)
  st.image(img_array)
  st.write(f"Predicted villian is {class_name}")
  st.write(f'Confidence: {confidence}')


#upload image from local system
image = st.file_uploader('Test Image', type = ['png', 'jpg'])

if st.button('Predict'):
  predict_image(image)
  
