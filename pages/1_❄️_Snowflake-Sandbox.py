import streamlit as st
from components.page_setting import generate_page

generate_page('Snowflake-Sandbox', '❄️')
st.write(st.session_state)
if st.session_state["authentication_status"]:
        st.write(f'Welcome *{st.session_state["name"]}*')
        st.title('Some content')
elif st.session_state["authentication_status"] == False:
        st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] == None:
        st.warning('Please enter your username and password')