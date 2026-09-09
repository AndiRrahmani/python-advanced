import pandas as pd
import streamlit as st


st.header("Displaying data frames")

data = pd.DataFrame({
    'Name':["Andi","Resa","Marsi"],
    'Age':['17','20','16']
})


st.dataframe(data)