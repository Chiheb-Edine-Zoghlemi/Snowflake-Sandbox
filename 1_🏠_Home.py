import streamlit as st
from components.page_setting import generate_page

def main():
    st.session_state.authentication_status = None
    generate_page('Home', '🏠')
    st.header('Introduction')
    st.text('')
    
    

if __name__ == "__main__":
    main()