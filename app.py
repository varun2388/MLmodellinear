import streamlit as st
import numpy as np
import pandas as pd
import joblib
from sklearn.datasets import load_boston

# Load the trained linear regression model
model = joblib.load('linear_regression_model.pkl')

# Load the Boston housing dataset
boston = load_boston()
feature_names = boston.feature_names

# Add a title and description to the Streamlit app
st.title("Boston Housing Price Prediction")
st.write("This app predicts the median value of owner-occupied homes in Boston using a linear regression model.")

# Create input fields for each feature variable
input_values = []
for feature in feature_names:
    value = st.number_input(f"Enter value for {feature}", value=0.0)
    input_values.append(value)

# Predict the house price using the input values
input_array = np.array(input_values).reshape(1, -1)
predicted_price = model.predict(input_array)

# Display the predicted house price
st.write(f"The predicted median value of the house is: ${predicted_price[0] * 1000:.2f}")
