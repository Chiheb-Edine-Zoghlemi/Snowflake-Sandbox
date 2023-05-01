import streamlit as st 
import pandas as pd 
import datetime
from time import sleep

def check_system(user_cnx):
    progress_text = "Checking the snowflake environment. Please wait."
    checks_list = [
        {'name': 'Cheking role ', 'sucess':'Role validation successful ✔️', 'error':'Role not found ❌',
         'func': user_cnx.check_role, 'creation': 'Creating the role', 'error_funct': None},
        {'name': 'Cheking user ', 'sucess':'User validation successful ✔️', 'error':'User not found ❌',
         'func': user_cnx.check_user, 'creation': 'Creating the user', 'error_funct': None},
        {'name': 'Cheking database ', 'sucess':'Database validation successful ✔️','error':'Database not found ❌',
          'func': user_cnx.check_database, 'creation': 'Creating the database', 'error_funct': None},
        {'name': 'Cheking warhouse ', 'sucess':'Warhouse validation successful ✔️', 'error':'Warhouse not found ❌',
         'func': user_cnx.check_warhouse, 'creation': 'Creating the warhouse', 'error_funct': None}
    ]

    my_bar = st.progress(0, text=progress_text)
    log = st.empty()
    for index,percent_complete in enumerate([25,50,75,100]):
        log.text(f"- {checks_list[index]['name']}" )
        sleep(1)
        check_status = checks_list[index]['func']()
        if check_status :
            log.text(f"- {checks_list[index]['sucess']}")
            sleep(1)
        else:
            log.text(f"- {checks_list[index]['error']}")
            sleep(1)
            log.text(f"- {checks_list[index]['creation']}")
            sleep(1)
        
        log.empty()
        my_bar.progress(percent_complete, text=progress_text)
    sleep(2)
    my_bar.empty()
    

def main():
    col1, col2 = st.columns(2)
    with col1:
        with st.form(key='my_form'):
            user_name = st.text_input(label='Benutzername/Username')
            expiry_date= str(st.date_input( "Ablaufdatum/Expiration Date", datetime.date.today()))
            submitted = st.form_submit_button(label='SETUP')
            if submitted:
                with st.spinner('Creating the environment'):
                    ret = run_procedure(user_name, expiry_date)
                    st.info(ret)
                    st.snow()
    with col2:
        st.text(' Current Active Tests ')
        with st.spinner('Fetching the Data'):
            data = load_test()
        df = pd.DataFrame(data, columns=("USERNAME","EXPIRATION DATE", "CREATION DATE"))
        st.table(df)
    st.markdown('<hr style="width:70%; margin: auto;" />', unsafe_allow_html=True)