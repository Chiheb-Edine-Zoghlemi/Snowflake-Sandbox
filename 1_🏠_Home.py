import streamlit as st
from components.page_setting import generate_page, footer

def main():
    generate_page('Home', '🏠')
    st.header('Introduction')
    st.text("""
    This app can be used to create fresh isolated snowflake sandboxes that can be used for testing, development or for technical job interviews. 
    Using the benefits of both Streamlit user-interface and snowflake objects and toolsets any user ( from any background ) can setup a sandbox with one click.  
    """)
    st.header('Usage Guide')
    st.text("""
    This usage of the app is very simple just config the app to work with your snowflake account by providing your credentials and the app will setup everything by itself.
    Then just provide the sandbox username and the expiration date in which you want the sandbox yo be deleted and the app will setup the sandbox.
    Setting up the sanbox consist of the following steps : 
    - Create a new database for the sandbox.
    - Create a role with the neccessary privillages to use the newly created sandbox.
    - Create a user with a default password xxxx that will be requested to change after the first sign in.
    - In case the user selected to upload data to the sandbox, for every uploaded file, a table with one variant column will be created which included the uploaded data.
    """)
    st.header('Next relase Features')
    st.text("""
    - Add imediate delete button for the sandbox.
    - Provid the option for the user to chose the number of user created for the sanbox ( instead of just one user by sandbox ) 
    - Add the possibility to assign user to multiple sandboxes.
    """)
    footer()
    
    

if __name__ == "__main__":
    main()