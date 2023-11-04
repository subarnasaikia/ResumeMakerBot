# import os
# from embedchain import App
from api import getKey
import streamlit as st


st.title("Resume Maker Bot...") 
api_key = getKey()
st.write(f"your api key is {api_key}")