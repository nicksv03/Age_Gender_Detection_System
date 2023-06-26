# Age Prediction with UTKFace Dataset

This repository contains a data science project that focuses on predicting the age of individuals based on the UTKFace Dataset. The project includes the following steps:

1. Data Preparation: The dataset consists of approximately 24,000 images, making it quite large. To enhance the model's speed and efficiency, the data is saved and compressed in TFRecords files. TFRecords provide an optimal storage solution for large datasets and facilitate training of Keras models. You can find more information on how and why to use TFRecords in the guide titled "A hands-on guide to TFRecords."

2. Image Processing and Model Prediction: The images are resized, and a pretrained model is utilized to predict the age of each person in the dataset. By leveraging the power of transfer learning, the model can make accurate age predictions based on facial features extracted from the images.

3. Streamlit App Development: To make it interactive and user-friendly, a Streamlit app has been built. You can upload your own photo and discover how old the model estimates you to be. For optimal results, it is recommended to upload a squared image containing only your face. Feel free to leave your feedback in the comments section regarding the accuracy of the predictions.

To get started, please refer to the notebook and code in this repository. Enjoy exploring the age prediction capabilities of the machine learning model!