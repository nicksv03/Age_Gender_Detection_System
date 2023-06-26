import streamlit as st
import tensorflow as tf
from PIL import Image


def main():
    st.header("Let me guess, How old are you?")
    st.write("Upload your photo and I will try to guess your age. (I'm not good at it though ;))")
    file = st.file_uploader("Upload Your Photo")
    if file is not None:
        st.image(file, width=300)
        image = Image.open(file)
        image = tf.image.resize(image, [224,224]) 
        image = tf.keras.preprocessing.image.img_to_array(image)
        image = image / 255.0      
        image = tf.expand_dims(image, axis=0)
        
        model = tf.keras.models.load_model("age_prediction/model_1.h5")
        age = model.predict(image)


        st.markdown('### I think you are {} years old'.format(int(age[0][0])))
        st.write('Curious about how I guessed your age? Check out my [Github] (https://github.com/nicksv03/Age_Gender_Detection_System)')


if __name__ == '__main__':
        main()
