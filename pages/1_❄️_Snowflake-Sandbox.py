import streamlit as st
from components.page_setting import generate_page, footer
from components.auth import login, logout


generate_page('Snowflake-Sandbox', '❄️')
st.write(st.session_state)

if 'authenticated' in st.session_state:
    if st.session_state.authenticated:
        st.write("You are currently authenticated.")
        logout()
    else:
        login()
else:
    login()




  

footer()
        