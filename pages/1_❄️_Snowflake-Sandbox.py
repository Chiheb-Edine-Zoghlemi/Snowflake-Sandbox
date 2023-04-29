import streamlit as st
from components.page_setting import generate_page, footer
from components.login import login


generate_page('Snowflake-Sandbox', '❄️')


if not st.session_state.get('authentication_status'):
        st.session_state.authentication_status = None



st.write(st.session_state["authentication_status"])

if st.session_state["authentication_status"]:
        st.write(f'Welcome *{st.session_state["authentication_status"]}*')
        st.title('Some content')
elif st.session_state["authentication_status"] == False:
        st.error('Invalid Credentials')
        login()
elif st.session_state["authentication_status"] == None:
        login()

footer()
        