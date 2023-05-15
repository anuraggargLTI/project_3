import streamlit as st
import streamlit.components.v1 as stc
from streamlit.components.v1 import html
from streamlit_option_menu import option_menu
import buyer
import seller
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
    st.header("Welcome Tom , Review Your Selections")

    key_df = pd.read_csv(Path("./state.csv"), dtype=str)
    keystate = key_df.iloc[0]['state']

    if keystate != '':
       # st.subheader("Welcome", st.session_state.usr)
       # st.subheader("Welcome Tom")
        for key in st.session_state.keys():
                vehicles_df = pd.read_csv(Path("./vehicles.csv"), dtype=str)
                df = pd.DataFrame(columns = vehicles_df.columns)
                for i in range(0,len(vehicles_df)):
                    line = vehicles_df.loc[[i]]
                    if str(key) == str(line.iloc[0]['id']) and str(line.iloc[0]['id']) != '' and len(key) == 10:
                        x = line.iloc[0]
                        if x["model"]:
                            st.markdown(CAR_HTML_TEMPLATE.format(x["model"].upper(), "$" + str(x["price"]), "Location: " + x["state"].upper(), x["id"]), unsafe_allow_html=True)
                        else:
                            st.markdown(CAR_HTML_TEMPLATE.format("UNKNOWN MODEL", "$" + str(x["price"]), "Location: " + x["state"].upper(), x["id"]), unsafe_allow_html=True)
                        with st.expander("Description"):
                            stc.html(CAR_DES_HTML_TEMP.format(x["description"]), scrolling=True)
        if st.button("Estimate the Price"):
            estimated_price = ml_model.ml_function(x["odometer"],x["year"],x["model"])
            st.write(estimated_price)  
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
        #if st.button("Return to Search"):
        #    for key in st.session_state.keys():
        #        if len(key) == 10:
        #            del st.session_state[key]
        #    key_df.iloc[0]['state'] = 'first'

        #st.write(key_df)
        #key_df.to_csv(Path("./state.csv"), index=False)



    
                    

    
