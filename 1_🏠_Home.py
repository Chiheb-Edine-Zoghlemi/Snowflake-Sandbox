import streamlit as st
from components.page_setting import generate_page, footer

def main():
    generate_page('Home', '🏠')
    st.header('Introduction')
    st.text('')
    footer()
    
    

if __name__ == "__main__":
    main()