import streamlit as st
from ml_model.ml_model import ml_function
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor

import numpy as np

import streamlit as st

st.title('Sellers Please Welcome')
st.write('Welcome your blockchain based car buying platform')

odometer = st.number_input("Enter the Mileage", key = "1")  
year = st.number_input("Enter the year", key = "2")   
model = st.text_input("Enter the model")  


if st.button('Estimate Price'):
    st.write(ml_function(odometer,year,model))










