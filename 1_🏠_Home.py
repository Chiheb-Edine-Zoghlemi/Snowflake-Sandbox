import streamlit as st
from sections.page_setting import generate_page, footer
import os 
from PIL import Image
def main():
    generate_page('Home', '🏠')
    st.header('Introduction')
    st.text("""
    This app can be used to create fresh isolated snowflake sandboxes that can be used for testing, development or for technical job interviews. 
    Using the benefits of both Streamlit user-interface and snowflake objects and tool sets any user ( from any background ) can set up a sandbox with one click. 
    """)
    st.info("""
    ⚠️ We do not store your credentials or track your usage, everything is stored in the streamlit session and will be deleted the moment you close the app.
    \n The [source code](https://github.com/Chiheb-Edine-Zoghlemi/Snowflake-Sandbox) of this app is public and you can check it yourself.
             """)
    st.header('Usage Guide')
    st.write("""
    The usage of this app is pretty stight forward.
    - Login using your snowflake account ( use an account with sufficant privillages to create databases and roles ).
    - Wait for the app to install the supporting objects.
    - Provide the usename and the expiration date of the sandbox.
    - Click setup button.
    - Repeat the two previous steps as much as needed.
    
    🔔 PS : For the  login the user must use a user with the **ACCOUNTADMIN** role or a role with sufficiant privillages to create users, roles and databaseobjects.
    """)

    st.header('Technical Guide')
    st.write("""
    After the first login the app will create the supporting object for the app. 
    Thes objects consist of the folowing:
    - A new role sandbox-monitor-role : this role will be used by the sandbox monitor user and will have the sufficent privillages to monitor and control and created sandboxes.
    - A new user sandbox-monitor : this user can be used to monitor the sandboxes created.
    - A new database sandbox-main : this database will contain all the supporting objects for the system.
    - A new table sandbox-log : this table will be used to monitor the created sandboxes and users. 
    - A new procedure sandbox-log : this procedure will be used to create the sandbox.
    - A new procedure sandbox-log : this procedure will be used to delete the sandbox and will be triggered by the task.
    - A new task sandbox-log : this task will run automatically every day at 00:00 and will delete the expired sandboxes.

    When setting up a new sanbox, the app will induct  the following steps : 
    - Create a role with the neccessary privillages to use the newly created sandbox.
    - Create a user with a default password 'Password123' that will be requested to change after the first log-in.
    - Create a new database for the sandbox.
    - Create a new table with one variant column for every file uploaded.
    
    - In case the user selected to upload data to the sandbox, for every uploaded file, a table with one variant column will be created which included the uploaded data.
    """)
    
    st.text("""In the following section, a quick presentation on """)
    cols = st.columns([0.5, 1, 0.5])
    with cols[1]:
        st.image(Image.open(os.path.join('static','SANDBOX_SETUP.png')), use_column_width=True)
    st.header('Next Relase Features')
    st.write("""
    - Add  the option to delete a sandbox immediatly.
    - Provide the option for the user to choose the number of sandbox users.
    - Add the possibility to assign user to multiple sandboxes.
    - Add a monitor by sandbox and provide the a usage limit by sandbox / sandbox user.
    - Upload data to the new created sandbox  (json / csv).
    """)
    footer()
    
    

if __name__ == "__main__":
    main()