import streamlit as st
import streamlit.components.v1 as stc
from streamlit.components.v1 import html
from streamlit_option_menu import option_menu
import buyer
import seller
import search
import buy_selection
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
    counter =0

    if 'key' not in st.session_state:
        st.session_state.key=counter
 #   st.write(st.session_state.key)
    if st.session_state.key==0:
         keystate="first"
         key_df.iloc[0]['state'] = 'first'
         key_df.to_csv(Path("./state.csv"), index=False)
         #st.session_state.key=counter+1
        #key_df.iloc[0]['state'] = "third"
        #key_df.to_csv(Path("./state.csv"), index=False)
    #if keystate == 'first':
    if keystate=="first" or keystate=="fourth":
        counter+=1
        st.session_state.key=counter
        st.title('Buyers Please Welcome')
        st.write('Welcome to your Blockchain based car buying platform')
        search.app()
        #key_df.iloc[0]["state"] = "second"
        #key_df.to_csv(Path("./state.csv"), index=False)
        #key_df = pd.read_csv(Path("./state.csv"), dtype=str)
        #keystate = key_df.iloc[0]['state']
        #st.write(keystate)
    elif keystate=="second":
        review_selection.app()
       # key_df.iloc[0]["state"] = "third"
       # key_df.to_csv(Path("./state.csv"), index=False)
        #key_df = pd.read_csv(Path("./state.csv"), dtype=str)
        #keystate = key_df.iloc[0]['state']
        #st.write(keystate)
    elif keystate=="third":
        st.write(keystate)
        buy_selection.app()
        key_df.iloc[0]["state"] = "first"
        key_df.to_csv(Path("./state.csv"), index=False)

   # if keystate == 'third':
    #    st.write(keystate)
     #   review_selection.app() 

    #if keystate == 'fourth':
    #    st.write(keystate)
        # buy_selection.app()


    # #read to db 
# conn = sqlite3.connect('vehicles.db')
# #vehicles_df = pd.read_csv(Path("./vehicles.csv"), dtype=str)
# vehicles_df = vehicles_df[["id","price","year","model","odometer","cylinders","paint_color","type","state"]]
# vehicles_df.to_sql('vehicles', conn, if_exists='append', index = False)

