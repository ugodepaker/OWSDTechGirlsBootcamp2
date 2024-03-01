import streamlit as st
import joblib
import pandas as pd

# Load the pre-trained model
@st.cache_data
def load_model():
    return joblib.load('rf_regressor.joblib')

model = load_model()

# Set background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFB6C1; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Welcome message
st.title('Welcome to the Plant Yield Prediction Platform!')
st.write("This platform is designed to help you predict plant yield based on parameters available")

# Introduction to advertising channels and costs
st.header('Plant Yield Parameters')
st.write("Before we make predictions, let's introduce you to the plant yield parameters ")
st.write("- Average Rainfall (mm)")
st.write("- Pesticides (tonnes)")
st.write("- Average Temperature")
st.write("Please input the values for plant yield parameters")

# Input fields for user input
st.sidebar.header('Plant Yield Parameters')
tv = st.sidebar.text_input('Average Rainfall (mm)', '600')
radio = st.sidebar.text_input('Pesticides (tonnes)', '9.5')
newspaper = st.sidebar.text_input('Average Temperature', '25.2')

# Submit button
if st.sidebar.button('Submit'):
    # Convert input values to float
    tv = float(tv)
    radio = float(radio)
    newspaper = float(newspaper)
    
    # Make predictions
    input_data = pd.DataFrame({'Rainfall': [RF], 'Pesticides': [Pest], 'Temperature': [TP]})
    prediction = model.predict(input_data)

    # Display prediction
    st.header('Plant Yield Prediction')
    st.success(f"Predicted Plant Yield: {prediction[0]}")
