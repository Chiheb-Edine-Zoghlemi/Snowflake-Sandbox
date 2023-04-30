
import streamlit as st
from src.snowflake import validated_credentials

def reset_session():
    st.session_state.authenticated = False

def check_user(username, password, account, warhouse, role):
    if st.session_state.get('login_btn'):
        if username and  password and  account and  warhouse:
                #st.session_state.authenticated =  True 
                auth_res = validated_credentials(username, password, account, warhouse, role)
                st.session_state.authenticated = auth_res 
                if not auth_res:
                    st.error("Please provide valid credentials")
        else:
                st.error("The username or password you entered is incorrect. Please try again.")

def logout():
    st.button("Logout", on_click=reset_session)
    st.session_state['login_btn'] = False


def login():
        
        col1, col2, col3, col4, col5 = st.columns(5)
        account = col1.text_input('Account').strip()
        username = col2.text_input('Username').strip()
        password  = col3.text_input('Password', type='password').strip()
        warhouse  = col4.text_input('Warhouse').strip()
        role  = col5.text_input('Role').strip()
        st.empty()
        st.session_state['login_btn'] = st.button("Login", on_click=check_user(username, password, account, warhouse, role))

