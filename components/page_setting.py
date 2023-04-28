import streamlit as st
from PIL import Image
import os 

def generate_page(title, emoji):
    title = title.strip()
    emoji = emoji.strip()
    img = Image.open(os.path.join('static','logo.png'))
    st.set_page_config(page_title=title,page_icon=img, layout="wide")
    st.title(f'{emoji} {title} Page')
    st.markdown(
        """
       <style>
        hr {background-color: #1a6ce7;}
        button[title="View fullscreen"]{visibility: hidden;}
        #MainMenu {visibility: hidden;}
        footer {visibility:hidden;}
        h1#"""+f'{title.lower()}-page'+""" {text-align: center;}
       </style>
       """,
        unsafe_allow_html=True,
    )  
    st.markdown('<hr style="width:70%; margin: auto;" />', unsafe_allow_html=True)

