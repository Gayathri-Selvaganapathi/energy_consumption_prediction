# Energy Consumption Prediction using Time Series Forecasting

## Project Overview
This project aims to predict energy consumption using time series forecasting techniques. The goal is to develop a model that can accurately forecast future energy consumption based on historical data. The project leverages machine learning models implemented in Python.

## Installation
Clone the repository:

```bash
git clone https://github.com/Gayathri-Selvaganapathi/energy_consumption_prediction.git
cd energy_consumption_prediction
```

## File Structure
1. app.py: The main script for running the energy consumption prediction model. This script handles data preprocessing, model training, and predictions.

2.time-series-forecasting-with-machine-learning.ipynb: A Jupyter Notebook that provides a detailed walkthrough of the time series forecasting process, including data exploration, model building, and evaluation.

## Requirements
To run this project, you'll need to install the following dependencies:

```bash

pip install -r requirements.txt
```
Make sure your environment is set up with the following packages:

## Data Preparation
The data for this time series prediction is downloaded from Kaggle (https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption) 
The data used for this project should be in a time series format, with timestamps and corresponding energy consumption values. The dataset is preprocessed to handle missing values, outliers, and other anomalies before being fed into the forecasting models.

# Model Training
The model training involves the following steps:

The model training process is detailed in the time-series-forecasting-with-machine-learning.ipynb file. The project primarily uses the XGBoost algorithm for predicting energy consumption. Different time series data formats and feature engineering techniques can be explored to potentially improve the model's accuracy.

## Running the Application
To run the application locally:

Ensure all dependencies are installed.Run the streamlt using below command

```bash
streamlit run app.py
```
This will start a local server where you can interact with the model through a simple streamlit GUI.