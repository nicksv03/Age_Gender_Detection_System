# Predicting Age and Gender using CNN on UTKFace Dataset

This project focuses on predicting the age and gender of individuals based on their facial images using deep learning techniques. The UTKFace dataset is utilized, which contains a large number of facial images labeled with age and gender information.

The code is implemented using Python and several popular libraries such as OpenCV, TensorFlow, Keras, NumPy, and Matplotlib. It follows the following steps:

1. Data Preparation:
   - Reads the images from the UTKFace dataset directory.
   - Resizes the images to a uniform size of 64x64 pixels.
   - Converts the images to grayscale.

2. Data Exploration:
   - Displays sample images from the dataset.
   - Shows a bar chart of age distribution.

3. Data Preprocessing:
   - Splits the dataset into training and testing sets.
   - Performs one-hot encoding of age groups and converts gender labels to binary.

4. Model Architecture:
   - Defines a convolutional neural network (CNN) model using Keras.
   - Utilizes convolutional and pooling layers to extract image features.
   - Applies dropout regularization to reduce overfitting.
   - Constructs separate branches for age and gender prediction.

5. Model Training and Evaluation:
   - Compiles the model with appropriate loss functions and metrics.
   - Trains the model on the training dataset.
   - Evaluates the model on the testing dataset.
   - Saves the trained model to a file.

6. Model Usage:
   - Provides helper functions to display and interpret results.
   - Defines age grouping and prediction functions.
   - Demonstrates the prediction on sample images.

Feel free to explore the code and adapt it to your own projects.
