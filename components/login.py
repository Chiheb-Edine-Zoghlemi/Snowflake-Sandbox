
import streamlit as st

def login():
    with st.form('login'):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            account = st.text_input('Account').strip()
        with col2:
            username = st.text_input('Username').strip()
        with col3:
            password = st.text_input('Password', type='password').strip()
        with col4: 
            warhouse = st.text_input('Warhouse').strip()

        if st.form_submit_button('Login'):
            if not account:
                st.warning('Please provide your snowflake account url | Example : zq73297.eu-west-9.aws  ')
            if not username:
                st.warning('Please provide your snowflake username')
            if not password:
                st.warning('Please provide your snowflake password')
            if not warhouse:
                st.warning('Please provide your snowflake warhouse')
            if account and username and password and warhouse:
                st.spinner

        else:
            st.warning('Please provide your snowflake credentials ')