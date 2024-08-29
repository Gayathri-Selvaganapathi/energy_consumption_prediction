import pandas as pd
import numpy as np
from datetime import datetime

# Function to predict energy consumption
def predict_energy(date_time_obj,loaded_model):
    # Extract features
    day_of_year = date_time_obj.timetuple().tm_yday
    hour = date_time_obj.hour
    day_of_week = date_time_obj.weekday()
    quarter = (date_time_obj.month - 1) // 3 + 1
    month = date_time_obj.month
    year = date_time_obj.year
    
    # Create a DataFrame with features as the model input
    input_data = pd.DataFrame({
        'dayofyear': [day_of_year],
        'hour': [hour],
        'dayofweek': [day_of_week],
        'quarter': [quarter],
        'month': [month],
        'year': [year]
    })
    
    # Predict energy consumption
    prediction = loaded_model.predict(input_data)
    
    return prediction[0]