import streamlit as st
from components.page_setting import generate_page
from components.login import login


generate_page('Snowflake-Sandbox', '❄️')

if st.session_state["authentication_status"]:
        st.write(f'Welcome *{st.session_state["name"]}*')
        st.title('Some content')
elif st.session_state["authentication_status"] == False:
        st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] == None:
        login()
        