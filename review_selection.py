import streamlit as st
import streamlit.components.v1 as stc
from streamlit.components.v1 import html
from streamlit_option_menu import option_menu
import buyer
import seller,connector,price_converter
import buy_selection
from ml_model import ml_model
import pandas as pd
from pathlib import Path
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode,DataReturnMode
#import sqlite3

PAGES = {
    "For Buyers": buyer,
    "For Sellers": seller
}

# html templates
CAR_HTML_TEMPLATE = """
<div style="color:white; width:100%; height:100%; margin:1px; padding:5px; position:sticky; border-radius:1px; border-bottom-right-radius: 1px;
box-shadow:0 0 1px 1px #eee; background-image: url('https://www.hdcarwallpapers.com/thumbs/2023/laferrari_sports_car-t2.jpg'); background-position: center center;
background-size: 280px; width: 225px; height: 175px; background-repeat:no-repeat; border-left: 5px solid #6c6c6c;">
<strong>
<p>{}</p>
<p>{}</p>
<p>{}</p>
<p>{}</p>
</strong>
</div>
"""

CAR_DES_HTML_TEMP = """
<div style='color:#818589'>
{}
<div>"""

# usernames and passwords >>>> HAS TO BE WRITTEN TO ANOTHER FILE EVENTUALLY AND THEN READ IN HERE 
usrs = ['username']
pwrd = ['123456789']
estimated_price=""
def app():
    st.header("Welcome Tom , Review your Selection")
    st.subheader(f"Your ETH balance is {connector.return_balance()} ETH")

    key_df = pd.read_csv(Path("./state.csv"), dtype=str)
    keystate = key_df.iloc[0]['state']

    if keystate != '':
       # st.subheader("Welcome", st.session_state.usr)
       # st.subheader("Welcome Tom")
        #for key in st.session_state.keys():
 
        for key in st.session_state.keys():
              #  st.write(key)
                vehicles_df = pd.read_csv(Path("./vehicles.csv"), dtype=str)
                for i in range(0,len(vehicles_df)):
                    line = vehicles_df.loc[[i]]
                    if str(key) == str(line.iloc[0]['id']) and str(line.iloc[0]['id']) != '' and len(key) == 10:
                        x = line.iloc[0]
                        #st.write(x)
                        if x["model"]:
                            st.markdown(CAR_HTML_TEMPLATE.format(x["model"].upper(), "$" + str(x["price"]), "Location: " + x["state"].upper(), x["id"]), unsafe_allow_html=True)
                        else:
                            st.markdown(CAR_HTML_TEMPLATE.format("UNKNOWN MODEL", "$" + str(x["price"]), "Location: " + x["state"].upper(), x["id"]), unsafe_allow_html=True)
                        with st.expander("Description"):
                            stc.html(CAR_DES_HTML_TEMP.format(x["description"]), scrolling=True)
    #st.write(x["odometer"])
        estimated_price = ml_model.ml_function(x["odometer"],x["year"],x["model"])
        estimated_price_eth=price_converter.getETHPrice(estimated_price)
        current_car_price = x["price"]
        #if st.button("Convert the Price"):
        #    converted_price = price_converter.getETHPrice(x["price"])
        st.write(f"The estimated purchase price of your car in dollars is {estimated_price} and in ETH is : {estimated_price_eth}")
                    
        st.write(f"Purchase price of your car is  {price_converter.getETHPrice(current_car_price)} ETH(based on today's conversation rate for ${current_car_price})") 
        
        #if st.button("Estimate the Price"):
        #estimated_price = ml_model.ml_function(x["odometer"],x["year"],x["model"])
           # st.write(estimated_price)
           # st.write("The estimated purchase price of your car is ${:,.0f}".format(estimated_price))
         #   converted_price=price_converter.getETHPrice(estimated_price)
         #   st.write(f"The estimated purchase price of your car in ETH is : {converted_price}")
            #+price_converter(estimated_price)+"ETH")  
       # if st.button("Convert the price to ETH"):
       #     if estimated_price!="":
       #         estimated_price = "100 ETH"
       #     else:
       #         estimated_price="50 ETH"
       
        if st.button("Buy Selections"):
            key_df.iloc[0]['state'] = "third"
            key_df.to_csv(Path("./state.csv"), index=False)
            #st.write(key_df)
            buy_selection.app()
        if st.button("Click twice to go back to Home page"):
            #st.write(key_df)
            key_df.iloc[0]['state'] = "first"
            key_df.to_csv(Path("./state.csv"), index=False)
            #buyer.app()
        #if st.button("Return to Search"):
        #    for key in st.session_state.keys():
        #        if len(key) == 10:
        #            del st.session_state[key]
        #    key_df.iloc[0]['state'] = 'first'

        #st.write(key_df)
        #key_df.to_csv(Path("./state.csv"), index=False)



    
                    

    
