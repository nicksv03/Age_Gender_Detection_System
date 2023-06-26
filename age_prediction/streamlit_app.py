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
        image = image.resize((224, 224))  # Resize the image to match the model's input size
        image = tf.keras.preprocessing.image.img_to_array(image)
        image = image / 255.0
        image = image[:, :, :3]  # Keep only the first three channels (RGB), discard the alpha channel if present
        image = tf.expand_dims(image, axis=0)

        try:
            model = tf.keras.models.load_model("age_prediction/model_1.h5")
            age = model.predict(image)
            predicted_age = int(age[0][0])
            st.markdown('### I think you are {} years old'.format(predicted_age))
        except Exception as e:
            st.error("An error occurred while predicting the age.")
            st.error(str(e))
        
        st.write('Curious about how I guessed your age? Check out my [Github](https://github.com/nicksv03/Age_Gender_Detection_System)')

if __name__ == '__main__':
    main()
