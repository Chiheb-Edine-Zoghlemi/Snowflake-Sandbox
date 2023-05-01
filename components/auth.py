
import streamlit as st
from src.snowflake import validated_credentials

def reset_session():
    st.session_state.authenticated = False
    del st.session_state['username'] 
    del st.session_state['password'] 
    del st.session_state['account'] 
    del st.session_state['warhouse']
    del st.session_state['role']

def check_user(username, password, account, warhouse, role):
    if username and  password and  account and  warhouse:
        auth_res = validated_credentials(username, password, account, warhouse, role)
        st.session_state.authenticated = auth_res 
        if not auth_res:
            st.error("Please provide valid credentials.")
        else:
            st.session_state['username'] = username
            st.session_state['password'] = password
            st.session_state['account'] = account
            st.session_state['warhouse'] = warhouse
            st.session_state['role'] = role
    else:
            st.error("Please provide your credentials.")

def logout():
    st.button("Logout", on_click=reset_session)
    


def login():
        if not st.session_state.authenticated:
            col1, col2, col3, col4, col5 = st.columns(5)
            account = col1.text_input('Account').strip()
            username = col2.text_input('Username').strip()
            password  = col3.text_input('Password', type='password').strip()
            warhouse  = col4.text_input('Warhouse').strip()
            role  = col5.text_input('Role').strip()
            button = st.button("Login", on_click=check_user, args=(username, password, account, warhouse, role))

