import streamlit as st
import streamlit.components.v1 as stc
from streamlit.components.v1 import html
from streamlit_option_menu import option_menu
import pandas as pd
from pathlib import Path
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode,DataReturnMode
#import sqlite3

def app():
    st.title('Sellers Please Welcome')
    st.write('Welcome your blockchain based car buying platform')

    vehicles_df = pd.read_csv(Path("./vehicles.csv"),dtype=str)        

    # st.write(vehicles_df['price'])                

    st.subheader("Sell Your Car!")
    st.write("Fill form below to add your car to our site.")
    
    with st.form(key='Sell Your Car', clear_on_submit=True):    
        idnum =st.text_input("10 Digit ID Number*")
        urlcode = st.text_input("URL*")
        region = st.text_input("Region", key = 'reg')
        region_url = st.text_input("Region URL")
        price = st.number_input("Price*", step=1000, value=25000)
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
        if st.form_submit_button("Post Your Car!"):
          if idnum and price and year and model and odometer and condition and cylinders and color and type and state and des:
            vehicles_df.loc[len(vehicles_df)] = [idnum, urlcode, region, region_url, str(price), year, manufacturer, model, condition, cylinders, fuel, 
            odometer, title_status, transmission, vin, drive, size, type, color, image_url, des, county, state, lat, long, date]
            vehicles_df.to_csv(Path("./vehicles.csv"), index=False)
            st.success("Your Car is Now Listed!")
          else: 
             st.error("Please Make Sure to List: 10 Digit ID Number, Price, Year, Model, Condition, Odometer, Cylinders, Type, Paint Color, Description, and State")
            

    


