import streamlit as st
import streamlit.components.v1 as stc
from streamlit.components.v1 import html
from streamlit_option_menu import option_menu
import pandas as pd
from pathlib import Path
from ml_model import ml_model
import login
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode,DataReturnMode
import random

#import sqlite3

def app():
    if 'in_search' in st.session_state:
        del st.session_state['in_search']

        # clears selections from search 
    for key in st.session_state.keys():
          if len(key) == 10:
                del st.session_state[key]
    key_df = pd.read_csv(Path("./state.csv"), dtype=str)
    keystate = key_df.iloc[0]['state']
  

    vehicles_df = pd.read_csv(Path("./vehicles.csv"),dtype=str)
    accounts_df = pd.read_csv(Path("./accounts.csv"), dtype=str)

    if keystate!="fourth":  
       st.title('Sellers Please Welcome')
       st.write('Welcome your blockchain based car buying platform')
       key_df.iloc[0]['state'] = 'fourth'
       key_df.to_csv(Path("./state.csv"), index=False)
       login.app()
    if keystate=="fourth":      
      st.title("Welcome Tom , Sell your car here")
      #st.subheader("Sell Your Car!")
      st.write("Fill form below to add your car to our site.")
    
      with st.form(key='Sell Your Car', clear_on_submit=False):    
        idnum =st.text_input("10 Digit ID Number*",random.randint(1111111111, 9999999999))
        urlcode = st.text_input("URL*")
        region = st.text_input("Region", key = 'reg')
        region_url = st.text_input("Region URL")
        price = st.number_input("Price*")
        year = st.text_input("Year*")
        manufacturer = st.radio("Manufacturer", ['ferrari'])
        model = st.text_input("Model*")
        condition = st.radio("Condition*", options=['new','excellent','good','fair','poor'])
        cylinders = st.text_input("Cylinders*")
        fuel = st.radio("Fuel", ['gas', 'hybrid', 'electric', 'other'])
        odometer = st.text_input("Odometer*", key ='odo')
        title_status = st.radio("Title Status", ['clean', 'rebuilt', 'salvage', 'other'])
        transmission = st.radio("Transmission", ['manual', 'automatic', 'other'])
        vin = st.text_input("VIN", key='vin')
        drive = st.radio("Drive", ['rwd', 'fwd', '4wd', 'other'])
        size = st.radio ("Size", ['full-size', 'mid-size', 'sub-compact', 'compact', 'other'])
        type = st.radio("Type*", ['coupe', 'convertible', 'other'])
        color = st.text_input("Paint Color*", key='col')
        image_url = st.text_input("Image Url", key='url')
        des = st.text_area("Description*", key = 'des')
        county = st.text_input("County")
        state = st.selectbox("State*", ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"])
        lat = st.text_input("Latitude")
        long = st.text_input("Longitude")
        date = st.date_input("Posting Date")
        estimated_price=""
        if st.form_submit_button("Estimate the price of your car"):
           if idnum and year and model and odometer :
            estimated_price = ml_model.ml_function(odometer,year,model)
            st.write(f"The estimated selling price of your car is {estimated_price}")
           else:
            st.error("Please Make Sure to provide: Year, Model, Odometer for us to estimate the price of your car!")

  # if estimated_price!="":
  #        if st.form_submit_button("Use this price"):
  #           price = st.text_input("Price*",estimated_price)
        if st.form_submit_button("Post Your Car!"):
          if idnum and price and year and model and odometer and condition and cylinders and color and type and state and des:
            ### logs to vehicle
            vehicles_df.loc[len(vehicles_df)] = [idnum, urlcode, region, region_url, str(price), year, manufacturer, model, condition, cylinders, fuel, 
            odometer, title_status, transmission, vin, drive, size, type, color, image_url, des, county, state, lat, long, date]
            vehicles_df.to_csv(Path("./vehicles.csv"), index=False)
            ### logs to user 
            st.success("Your Car is Now Listed!")
            key_df.iloc[0]['state'] = 'first'
            key_df.to_csv(Path("./state.csv"), index=False)
          else: 
             st.error("Please Make Sure to List: 10 Digit ID Number, Price, Year, Model, Condition, Odometer, Cylinders, Type, Paint Color, Description, and State")
      

    


