import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import pickle
from functions import predict_energy

# Load the pre-trained model
loaded_model = pickle.load(open('time_series_model.sav', 'rb'))

# Streamlit UI
st.title('Energy Consumption Prediction')

# Input: Date and Time using Streamlit's date_input and time_input
selected_date = st.date_input('Select Date')
selected_time = st.time_input('Select Time')

# Combine selected date and time into a datetime object
if selected_date and selected_time:
    date_time_obj = datetime.combine(selected_date, selected_time)

if st.button('Predict'):
    try:
        prediction = predict_energy(date_time_obj,loaded_model)
        st.success(f'Predicted Energy Consumption: {prediction:.2f} kWh')
    except Exception as e:
        st.error(f"Error: {e}")
