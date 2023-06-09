import streamlit as st
import tensorflow as tf
from PIL import Image

def main():
    st.header("Age and Gender Detection")
    st.write("Upload an Image")
    file = st.file_uploader("Please upload an image file", type=["jpg", "png"])
    if file is not None:
        st.image(file, width = 300)
        image = Image.open(file)
        image = image.resize((224, 224))
        image = tf.keras.preprocessing.image.img_to_array(image)
        image = image/255.0
        image = image.expand_dims(image, axis=0)

        model = tf.keras.models.load_model("agds.h5")
        age = agds.predict(image)
        st.markdown("## You're %i years old according to our model!" %age[0][0])

if __name__ == '__main__':
	main()