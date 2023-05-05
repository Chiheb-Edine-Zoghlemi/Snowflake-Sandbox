import streamlit as st
from sections.page_setting import generate_page, footer
from PIL import Image
def main():
    generate_page('Home', '🏠')
    st.header('Introduction')
    st.text("""
    This app can be used to create fresh isolated snowflake sandboxes that can be used for testing, development or for technical job interviews. 
    Using the benefits of both Streamlit user-interface and snowflake objects and tool sets any user ( from any background ) can set up a sandbox with one click. 
    """)
    st.header('Usage Guide')
    st.write("""
    The usage of this app is pretty stight forward.
    - Login using your snowflake account ( use an account with sufficant privillages to create databases and roles ).
    - Wait for the app to install the supporting objects.
    - Provide the usename and the expiration date of the sandbox.
    - Click setup button.
    - Repeat the two previous steps as much as needed.
    """)
    st.header('Technical Guide')
    st.write("""
    This usage of the app is very simple. as first step you have to provide your snowflake account. This account must have the sufficent role privillages ( to create databases, roles and user ) something like ACCOUNTADMIN role will be more than sufficiant.
    After the login the app will create the supporting object for the system to run. thes objects consist of the folowing:
    - A new role sandbox-monitor-role : this role will be used by the sandbox monitor user and will have the sufficent privillages to monitor and control and created sandboxes.
    - A new user sandbox-monitor : this user can be used to monitor the sandboxes created.
    - A new database sandbox-main : this database will contain all the supporting objects for the system.
    - A new table sandbox-log : this table will be used to monitor the created sandboxes and users. 

    just config the app to work with your snowflake account by providing your credentials and the app will setup everything by itself.
    Then just provide the sandbox username and the expiration date in which you want the sandbox yo be deleted and the app will setup the sandbox.
    Setting up the sanbox consist of the following steps : 
    - Create a new database for the sandbox.
    - Create a role with the neccessary privillages to use the newly created sandbox.
    - Create a user with a default password 'Password123' that will be requested to change after the first sign in.
    - In case the user selected to upload data to the sandbox, for every uploaded file, a table with one variant column will be created which included the uploaded data.
    """)
    
    st.text("""In the following section, a quick presentation on """)
    cols = st.columns([0.5, 1, 0.5])
    with cols[1]:
        st.image(Image.open('static\SANDBOX_SETUP.png'), use_column_width=True)
    st.header('Next Relase Features')
    st.text("""
    - Add immediate delete button for the sandbox.
    - Provide the option for the user to choose the number of user created by sandbox ( instead of just one user by sandbox ) 
    - Add the possibility to assign user to multiple sandboxes.
    - Add a monitor by sandbox and provide the a usage limit by sandbox / sandbox user
    """)
    footer()
    
    

if __name__ == "__main__":
    main()