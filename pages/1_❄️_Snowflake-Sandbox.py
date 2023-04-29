import streamlit as st
from components.page_setting import generate_page, footer, load_cookies
from components.login import login
import extra_streamlit_components as stx

generate_page('Snowflake-Sandbox', '❄️')

cookie_manager = stx.CookieManager()

load_cookies(cookie_manager)
st.write(st.session_state,'---' ,cookie_manager.get_all())

login(cookie_manager)
st.write(bool(st.session_state['authentication_status']))
if cookie_manager.get('authentication_status'):
        st.write('sahit')
        if st.button('Logut'):
                cookie_manager.set('authentication_status',None) 
elif cookie_manager.get('authentication_status') == False:
        st.error('Invalid Credentials')
else:
        st.warning('Please provide your snowflake credentials ')







  

footer()
        