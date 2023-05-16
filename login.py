import streamlit as st
import streamlit.components.v1 as stc
from streamlit.components.v1 import html
from streamlit_option_menu import option_menu
import review_selection
import buyer,seller
import pandas as pd
from pathlib import Path
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode,DataReturnMode
#import sqlite3

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


def app():
    
    key_df = pd.read_csv(Path("./state.csv"), dtype=str)
    keystate = key_df.iloc[0]['state']
    accounts_df = pd.read_csv(Path("./accounts.csv"), dtype=str)
    

    placeholder = st.empty()
    if 'usr' not in st.session_state:
        with placeholder.form("login"):
            st.markdown("#### Enter your credentials")
            usr = st.text_input("Username")
            password = st.text_input("Password", type="password")
           # st.session_state['usr'] = usr
            submit = st.form_submit_button("Log Me in")
           # st.session_state['usr'] = usr
            if submit:  ### based on accounts.csv now
             st.session_state['usr'] = usr
             st.write("hello")
             mu = accounts_df["username"].str.contains(usr)
             accounts_df = accounts_df[mu]
             mp = accounts_df["password"].str.contains(password)
             accounts_df = accounts_df[mp]
             if len(accounts_df) != 0: 
                st.success("Login Successful")
             st.session_state['usr'] = usr
             if keystate=="fourth":
                 seller.app()
             #key_df.iloc[0]["state"] = "second"
             #key_df.to_csv(Path("./state.csv"), index=False)
             #buyer.app()
           # if st.session_state['in_search'] == 'True':
        #    if 'in_search' not in st.session_state:
        #            key_df.iloc[0]['state'] = 'second'
        #            key_df.to_csv(Path("./state.csv"), index=False)

        #elif submit:
        #    st.error("Login Failed")
    #else:
    #    if st.button("Logout"):
    #        del st.session_state['usr']
    
    
