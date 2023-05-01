import streamlit as st
from components.page_setting import generate_page, footer
from components.auth import login, logout
from components.app import main, check_system
from src.snowflake import snowcon


generate_page('Snowflake-Sandbox', '❄️')


if 'authenticated' in st.session_state:
    if st.session_state.authenticated:
        user_cnx = snowcon(st.session_state.username,
                           st.session_state.password,
                           st.session_state.account,
                           st.session_state.warhouse,
                           st.session_state.role)
        check_system(user_cnx)
        logout()
        # main()
    else:
        login()
else:
    st.session_state['authenticated'] = None
    login()




  

footer()
        