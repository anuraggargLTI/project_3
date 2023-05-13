import streamlit as st
import streamlit.components.v1 as stc
from streamlit.components.v1 import html
from streamlit_option_menu import option_menu
import buyer
import seller
import search
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
    st.title('Buyers Please Welcome')
    st.write('Welcome to your Blockchain based car buying platform')
    search.app()

            



    
    # #read to db 
# conn = sqlite3.connect('vehicles.db')
# #vehicles_df = pd.read_csv(Path("./vehicles.csv"), dtype=str)
# vehicles_df = vehicles_df[["id","price","year","model","odometer","cylinders","paint_color","type","state"]]
# vehicles_df.to_sql('vehicles', conn, if_exists='append', index = False)

