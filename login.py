import streamlit as st
import streamlit.components.v1 as stc
from streamlit.components.v1 import html
from streamlit_option_menu import option_menu
import buyer
import seller
import review_selection
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

def app():
    
    key_df = pd.read_csv(Path("./state.csv"), dtype=str)
    keystate = key_df.iloc[0]['state']

    placeholder = st.empty()
    if keystate =='second':
        with placeholder.form("login"):
            st.markdown("#### Enter your credentials")
            usr = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Login")
        
        if submit and usr == 'Tom' and password == '123456':
            st.success("Login Successful")
            key_df.iloc[0]['state'] = 'third'
            key_df.to_csv(Path("./state.csv"), index=False)
            keystate = key_df.iloc[0]['state']
            review_selection.app() 
        elif submit and usr != 'Tom':
            st.error("Login Failed")
        elif submit and password != '123456':
            st.error("Login Failed")
        

    
    
