
import streamlit as st
from src.snowflake import validated_credentials



def login(cookie_manager):
    if  not st.session_state['authentication_status'] :
        with st.form('login'):
            credits = {}
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                credits['account'] = st.text_input('Account').strip()
            with col2:
                credits['username']  = st.text_input('Username').strip()
            with col3:
                credits['password']  = st.text_input('Password', type='password').strip()
            with col4: 
                credits['warhouse']  = st.text_input('Warhouse').strip()
            with col5: 
                credits['role']  = st.text_input('Role').strip()
            if st.form_submit_button('Login') :
                for key in credits:
                    cookie_manager.delete(key)
                    cookie_manager.set(key,credits[key])
                     
                cookie_manager.set('authentication_status',True) 
                