import streamlit as st
from PIL import Image
import os 
import streamlit.components.v1 as component


        
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

def footer():
    footer="""
    <style>
    .footer {
    color : white ; 
    font-family: "Source Sans Pro", sans-serif;
    text-align: center;
    }
    .footer a{ 
        color : white; 
        text-decoration: none;
    }
    .footer a:hover{ 
        color : #1a6ce7; 
    }
     .footer span {
     color : red ; 
     }

    </style>
    <footer class="footer">
    <p>Developed with <span> ❤ </span> by <a style='display: block; text-align: center;' href="https://www.linkedin.com/in/chihebedinezoghlemi/" target="_blank">Chiheb Eddine Zoghlami</a></p>
    </footer>
    """
    component.html(footer)