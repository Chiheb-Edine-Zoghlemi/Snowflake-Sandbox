
import streamlit as st
from src.snowflake_config import validated_credentials

def reset_session():
    st.session_state.authenticated = False
    del st.session_state['username'] 
    del st.session_state['password'] 
    del st.session_state['account'] 
    del st.session_state['warhouse']
    
    del st.session_state['check_status']

def check_user(username, password, account, warhouse):
    if username and  password and  account and  warhouse:
        auth_res = validated_credentials(username, password, account, warhouse)
        st.session_state.authenticated = auth_res 
        if not auth_res:
            st.error("Please provide valid credentials.")
        else:
            st.session_state['username'] = username
            st.session_state['password'] = password
            st.session_state['account'] = account
            st.session_state['warhouse'] = warhouse
            
    else:
            st.error("Please provide your credentials.")

def logout():
    st.button("Logout", on_click=reset_session)
    


def login():
        if not st.session_state.authenticated:
            
            col1, col2, col3, col4 = st.columns(4)
            account = col1.text_input('Account').strip()
            username = col2.text_input('Username').strip()
            password  = col3.text_input('Password', type='password').strip()
            warhouse  = col4.text_input('Warhouse').strip()
           
            button = st.button("Login", on_click=check_user, args=(username, password, account, warhouse))
            st.write('Please read the [usage guide page](/) for insctruction on the account requirements.')

