import streamlit as st 
import pandas as pd 
import datetime
from time import sleep

def check_system(user_cnx):
    progress_text = "Checking the snowflake environment. Please wait."
    checks_list = [
        {'name': 'role','checking_func': user_cnx.check_role,  'creation_funct': user_cnx.create_role},
        {'name': 'user','checking_func': user_cnx.check_user, 'creation_funct': user_cnx.create_user},
        {'name': 'warhouse','checking_func': user_cnx.check_warhouse,  'creation_funct': user_cnx.create_warehouse},
        {'name': 'database', 'checking_func': user_cnx.check_database, 'creation_funct': user_cnx.create_database},
        {'name': 'log table','checking_func': user_cnx.check_log_table, 'creation_funct': user_cnx.create_log_table},
        {'name': 'sandbox creation procedure','checking_func': user_cnx.check_log_table, 'creation_funct': user_cnx.create_creation_procedure},
        {'name': 'sandbox removing procedure','checking_func': user_cnx.check_log_table, 'creation_funct': user_cnx.create_cleaning_procedure},
        {'name': 'sandbox removing task','checking_func': user_cnx.check_log_table, 'creation_funct': user_cnx.create_task}
    ]

    my_bar = st.progress(0, text=progress_text)
    log = st.empty()
    for index,percent_complete in enumerate([20,40,60,80,100]):
        log.text(f"- Checking {checks_list[index]['name']}" )
        sleep(1)
        check_status = checks_list[index]['checking_func']()
        if check_status :
            log.text(f"- Validation {checks_list[index]['name']} successful ✔️")
            sleep(1)
        else:
            log.text(f"- Validation {checks_list[index]['name']} failed ❌")
            sleep(1)
            log.text(f"- Creating {checks_list[index]['name']} 🛠️")
            sleep(1)
            creation_status, creation_log = checks_list[index]['creation_funct']()
            if creation_status:
                log.text(f"- Creation validation {checks_list[index]['name']} successful ✔️")
            else:
                log.text(f"- {creation_log}")
        
        log.empty()
        my_bar.progress(percent_complete, text=progress_text)
    my_bar.empty()
    

def main(user_cnx):
    col1, col2 = st.columns(2)
    with col1:
        with st.form(key='my_form'):
            user_name = st.text_input(label='Sandbox user')
            expiry_date= str(st.date_input( "Expiration Date", datetime.date.today()))
            submitted = st.form_submit_button(label='SETUP')
            if submitted:
                with st.spinner('Creating the environment'):
                    ret = user_cnx.run_procedure(user_name, expiry_date)
                    st.info(ret)
                    st.snow()
    with col2:
        st.text(' Current Active Tests ')
        with st.spinner('Fetching the Data'):
            data = user_cnx.load_sandboxes()
        df = pd.DataFrame(data, columns=("USERNAME","EXPIRATION DATE", "CREATION DATE"))
        st.table(df)
    st.markdown('<hr style="width:70%; margin: auto;" />', unsafe_allow_html=True)