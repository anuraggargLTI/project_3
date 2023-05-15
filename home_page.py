import streamlit as st
import streamlit.components.v1 as stc
from streamlit.components.v1 import html
from streamlit_option_menu import option_menu
import buyer
import seller
import login
import buy_selection
import review_selection
import search
import pandas as pd
from pathlib import Path
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode,DataReturnMode
#import sqlite3




# hides streamlit logos
hide_default_format = """
       <style>
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

#pages
PAGES = {
    "For Buyers": buyer,
    "For Sellers": seller, 
  # "Login": login
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

with st.sidebar:
        choose = option_menu("Navigation", list(PAGES.keys()),
                         icons=['arrow-right-circle', 'arrow-right-circle', 'arrow-right-circle'],
                         menu_icon="dash", default_index=0,
                         styles={
        "container": {"padding": "5!important"},
        "icon": {"font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

page = PAGES[choose]
#key_df = pd.read_csv(Path("./state.csv"), dtype=str)
#if key_df.iloc[0]['state']  == "first":
page.app()
#elif key_df.iloc[0]['state']  == "second":
#     review_selection.app()
#elif key_df.iloc[0]['state']  == "third":
#    buy_selection.app()   
#else:
#    key_df.iloc[0]['state'] = 'first'
#    key_df.to_csv(Path("./state.csv"), index=False)
#    page.app()
#if page == login:
#        key_df.iloc[0]['state'] = 'second'
#        key_df.to_csv(Path("./state.csv"), index=False)
        #page.app()
#        login.app()
        #review_selection.app()
#else:
#        key_df.iloc[0]['state'] = 'first'
#key_df.to_csv(Path("./state.csv"), index=False)
#if key_df.iloc[0]['state']  == "second":
#    review_selection.app()
#if key_df.iloc[0]['state']  == "third":
#    buy_selection.app()     

