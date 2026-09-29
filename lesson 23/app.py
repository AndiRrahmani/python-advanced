import streamlit as st
import requests
import pandas as pd

st.title("Project menagment App")

st.header("Add a Developer")
dev_name = st.text_input("Developer Name")
dev_experience = st.number_input("Experience (Years)", min_value=0,max_value=50, value=0)

if st.button("Create Developer"):
    dev_data = {"name": dev_name, "experience": dev_experience}
    responses = requests.post("https://localhost:8000/developers", json=dev_data)
    st.json(responses.json())




st.header("Add a Project")
proj_title = st.text_input("Project Title")
proj_desc = st.text_input("Project Description")
proj_lang = st.text_input("Language Used (Coma-seperated)")
lead_dev_name = st.text_input("Lead Developer Name")
lead_dev_exp = st.number_input("Lead Experience (Years)", min_value=0,max_value=50, value=0)

if st.button("Create Project"):
    lead_dev_data = {"name": dev_name, "experience": dev_experience}
    proj_data = {
        "title": proj_title,
        "description": proj_desc,
        "language": proj_lang.split(","),
        "lead_developer": lead_dev_data
    }
    responses = requests.post("https://localhost:8000/projects", json=proj_data)
    st.json(responses.json())




















