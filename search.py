import streamlit as st
import streamlit.components.v1 as stc
from streamlit.components.v1 import html
from streamlit_option_menu import option_menu
import buyer
import seller
import buy_selection
import review_selection
import login
import pandas as pd
from pathlib import Path
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode,DataReturnMode
import csv
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

   # if keystate == 'first':
    if keystate !="":
        st.subheader("Welcome to Ferravana , blockchain based ferrari trading platform!")
        name = st.text_input("Search Ferraris", value="")
        vehicles_df = pd.read_csv(Path("./vehicles.csv"), dtype=str) 
# filter from search 
        col1, col2 = st.columns([2,1])

        with col1:
                if name:
                        vehicles_df = pd.read_csv(Path("./vehicles.csv"), dtype=str)  
                        vehicles_df = vehicles_df[["id","price","year","model","odometer","condition","cylinders","paint_color","type","state", "description"]] 
                        m1 = vehicles_df["id"].str.contains(name)
                        m2 = vehicles_df["price"].str.contains(name)
                        m3 = vehicles_df["year"].str.contains(name)
                        m4 = vehicles_df["model"].str.contains(name)
                        m5 = vehicles_df["odometer"].str.contains(name)
                        m6 = vehicles_df["cylinders"].str.contains(name)
                        m7 = vehicles_df["paint_color"].str.contains(name)
                        m8 = vehicles_df["type"].str.contains(name)
                        m9 = vehicles_df["state"].str.contains(name)
                        m10 = vehicles_df["condition"].str.contains(name)
                        vehicles_df = vehicles_df[m1 | m2 | m3 | m4 | m5 | m6 | m7 | m8 | m9 | m10]

        # display number of results
                        st.success("Found {} results for \"{}\"".format(str(len(vehicles_df)), name))

                        gb = GridOptionsBuilder.from_dataframe(vehicles_df)
                        gb.configure_default_column(enablePivot=False, enableValue=True, enableRowGroup=True)
                        gb.configure_selection(selection_mode="multiple", use_checkbox=True, rowMultiSelectWithClick=True)
                        gb.configure_side_bar(filters_panel=True, columns_panel=True) # Add configuration
                        gridoptions = gb.build()
                        grid_response = AgGrid(
                                vehicles_df,
                                gridOptions=gridoptions,
                                data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
                                update_mode=GridUpdateMode.SELECTION_CHANGED,
                                allow_unsafe_jscode=True,
                                fit_columns_on_grid_load=False,
                                theme='streamlit', 
                                enable_enterprise_modules=True,
                                height=350, 
                                width='100%',
                                use_checkbox=True,
                                header_checkbox_selection_filtered_only=True,
                                deltaRowDataMode=True
                            )
        # creates two columns
        with col2:
                if name:
                    st.subheader("Selected Listings:")
                    for row in grid_response["selected_rows"]:
                        name = str(row['id'])
                        if name not in st.session_state:
                            st.session_state[name] = name
                        if row["model"]:
                            st.markdown(CAR_HTML_TEMPLATE.format(row["model"].upper(), "$" + str(row["price"]), "Location: " + row["state"].upper(), row["id"]), unsafe_allow_html=True)
                        else:
                            st.markdown(CAR_HTML_TEMPLATE.format("UNKNOWN MODEL", "$" + str(row["price"]), "Location: " + row["state"].upper(), row["id"]), unsafe_allow_html=True)
                        with st.expander("Description"):
                            stc.html(CAR_DES_HTML_TEMP.format(row["description"]), scrolling=True)
                    if st.button(label="Check Out"):
                        st.session_state['in_search'] = 'True'
                        login.app()
                        key_df.iloc[0]['state'] = 'second'
                        key_df.to_csv(Path("./state.csv"), index=False)
                       # if 'usr' not in st.session_state:
                          #  login.app()
                            #review_selection.app()

                        #else:
                        #    key_df.iloc[0]['state'] = 'second'
                        #    key_df.to_csv(Path("./state.csv"), index=False)
                        #    keystate = key_df.iloc[0]['state']
                            #review_selection.app()
    
   # if keystate == 'second':
                    
   
  #  if keystate == 'fourth':
   #         buy_selection.app()
