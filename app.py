import os
from embedchain import App
from api import getKey
import streamlit as st



api_key = getKey()
# if api_key != "":
os.environ['OPENAI_API_KEY'] = api_key
app = App()


st.title("Resume Maker Bot...") 


# linkedIn_link = st.text_input("Enter your LinkedIn profile URL: ")
# linkedIn_link = 'Enter your linkedIn profile  URL'
# app.add(linkedIn_link, data_type='web_page')

app.add('./data/Profile_Subarna.pdf', data_type='pdf_file')



prompt =st.text_input("Enter your prompt....")

Context = f"""
Hi, Act as a resume builder and based on data available create a resume for software engineer
{prompt}
"""

if prompt:
    response = app.query(Context)
    st.write(response)