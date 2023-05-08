import streamlit as st
import buyer
import seller
import pandas as pd
from pathlib import Path
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode,DataReturnMode


PAGES = {
    "Buyer": buyer,
    "Seller": seller
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
form = st.form(key='search-form')
name = form.text_input(label='Search your ferrari')
submit = form.form_submit_button(label='Search')
if submit:
    vehicles_df = pd.read_csv(Path("./vehicles.csv"))
    vehicles_df = vehicles_df[["id","price","year","model","odometer","cylinders","paint_color","type","state"]]
    vehicles_df["id"]=vehicles_df["id"].astype(str)
    vehicles_df["year"]=vehicles_df["year"].astype(str)
    gb = GridOptionsBuilder.from_dataframe(vehicles_df)
    gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
    gb.configure_default_column(enablePivot=True, enableValue=True, enableRowGroup=True)
    gb.configure_selection(selection_mode="multiple", use_checkbox=True)
    gb.configure_side_bar() #Add a sidebar
    gridoptions = gb.build()
    grid_response = AgGrid(
                        vehicles_df,
                        gridOptions=gridoptions,
                        data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
                        update_mode=GridUpdateMode.MODEL_CHANGED,
                        fit_columns_on_grid_load=False,
                        theme='blue', #Add theme color to the table
                        enable_enterprise_modules=True,
                        height=350, 
                        width='100%',
                        use_checkbox=True,
                        header_checkbox_selection_filtered_only=True,
                        deltaRowDataMode=True
                        )
    filterbtn = st.button('Get filtered data')
    if filterbtn:
       st.table(grid_response['data'])
    #data = grid_response['data']
    #selected = grid_response['selected_rows'] 
    #st.dataframe(selected) #Pass th   
   # st.write(selected_df) 





