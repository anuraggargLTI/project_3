import streamlit as st
import streamlit.components.v1 as stc
from streamlit.components.v1 import html
from streamlit_option_menu import option_menu
import buyer
import seller
import login
import search
import pandas as pd
from pathlib import Path
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode,DataReturnMode
import csv
#import sqlite3


def app():
    key_df = pd.read_csv(Path("./state.csv"), dtype=str)
    keystate = key_df.iloc[0]['state']

    if keystate == 'fourth':
        for key in st.session_state.keys():
                if len(key) == 10:
                    vehicles_df = pd.read_csv(Path("./vehicles.csv"), dtype=str)
                    df = pd.DataFrame(columns = vehicles_df.columns)
                    for i in range(0,len(vehicles_df)):
                        line = vehicles_df.loc[[i]]
                        if str(key) == str(line.iloc[0]['id']) and str(line.iloc[0]['id']) != '':
                            x = line.iloc[0]
                            st.write(x)