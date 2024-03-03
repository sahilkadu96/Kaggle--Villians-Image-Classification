# Kaggle--Villians-Image-Classification/
 - Dataset downloaded from: https://www.kaggle.com/datasets/rogeriovaz/villains-image-classification . 
 - The dataset contains images of **5 villians - Darth Vader, Green Goblin, Joker, Thanos, Venom.**
 - Used **VGG16 model through Transfer Learning.** 
 - Refer **Villian_Image_classification_using_VGG16.ipynb** for more info about model building.
 - We imported the VCG16 model from Keras, chopped of the top layer & aded our customised Dense layer (softmax activation with 5 units for 5 clases) as the output.
 - After training for 10 epochs, we get **validation accuracy as 86.67%**
 - Deployed on Streamlit. Refer **app.py**

# STreamlit interface
![image](https://github.com/sahilkadu96/Kaggle--Villians-Image-Classification/assets/106151994/39ebb98e-25a8-466d-8b2a-19576baa50f9)

