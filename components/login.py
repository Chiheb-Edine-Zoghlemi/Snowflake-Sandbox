
import streamlit as st
from src.snowflake import validated_credentials
def login():
    with st.form('login'):
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            account = st.text_input('Account').strip()
        with col2:
            username = st.text_input('Username').strip()
        with col3:
            password = st.text_input('Password', type='password').strip()
        with col4: 
            warhouse = st.text_input('Warhouse').strip()
        with col5: 
            role = st.text_input('Role').strip()
        submit_form = st.form_submit_button('Login')
        if submit_form :
            if not account:
                st.warning('Please provide your snowflake account url | Example : zq73297.eu-west-9.aws  ')
            if not username:
                st.warning('Please provide your snowflake username')
            if not password:
                st.warning('Please provide your snowflake password')
            if not warhouse:
                st.warning('Please provide your snowflake warhouse')
            if account and username and password and warhouse:
                with st.spinner():
                    status = validated_credentials(username, password, account, warhouse, role)
                st.session_state["authentication_status"] =  status 
                     

        else:
            st.warning('Please provide your snowflake credentials ')