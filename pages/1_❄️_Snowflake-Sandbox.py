import streamlit as st
from sections.page_setting import generate_page, footer
from sections.auth import login, logout
from sections.app import main, check_system
from src.snowflake_config   import snowcon


generate_page('Snowflake-Sandbox', '❄️')


if 'authenticated' in st.session_state:
    if st.session_state.authenticated:
        user_cnx = snowcon(st.session_state.username,
                           st.session_state.password,
                           st.session_state.account,
                           st.session_state.warhouse,
                           st.session_state.role)
        logout()
        if 'check_status' not in st.session_state:
            check_status = check_system(user_cnx)
        else:
            check_status = st.session_state.get('check_status')
        
        if check_status:
            main(user_cnx)
        else:
            st.error(' [  SYSTEM  SETUP FAILED ] : Please make sure to follow the guiddlines provided in the Home page')
            
        
        
    else:
        login()
else:
    st.session_state['authenticated'] = None
    login()




  

footer()
        