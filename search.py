import streamlit as st
import pandas as pd
from pathlib import Path
def app(search):
    st.write(search)

vehicles_df = pd.read_csv(Path("./vehicles.csv"))
st.write(vehicles_df)