# Snowflake-Sandbox

## General Description

This app can be used to create fresh isolated snowflake sandboxes that can be used for testing, development or for technical job interviews.
Using the benefits of both Streamlit user-interface and snowflake objects and tool sets any user ( from any background ) can set up a sandbox with one click.

## Features

In the following list of implemented feautres :

1. Link the app to a signle snowflake environment (inprogress)
    1. connection validation (inprogress)
    2. install the config scripts in the destination  environment (inprogress)

Features that will be implemented :

1. Link the app to a multiple snowflake environments

## Usage Guide

The usage of this app is pretty stight forward.
    - Login using your snowflake account ( use an account with sufficant privillages to create databases and roles ).
    - Wait for the app to install the supporting objects.
    - Provide the usename and the expiration date of the sandbox.
    - Click setup button.
    - Repeat the two previous steps as much as needed.

🔔 PS : For the  login the user must use a user with the **ACCOUNTADMIN** role or a role with sufficiant privillages to create users, roles and databaseobjects.

## Technical Description

After the first login the app will create the supporting object for the app. 
Thes objects consist of the folowing:

- A new role sandbox-monitor-role : this role will be used by the sandbox monitor user and will have the sufficent privillages to monitor and control and created sandboxes.
- A new user sandbox-monitor : this user can be used to monitor the sandboxes created.
- A new database sandbox-main : this database will contain all the supporting objects for the system.
- A new table sandbox-log : this table will be used to monitor the created sandboxes and users.
- A new warhouse SANDBOX_MONITOR_WH : this warhouse can be used by the sandbox monitor user.
- A new procedure SANBOX_SETUP : this procedure will be used to create the sandbox.
- A new procedure SANDBOX_DROP : this procedure will be used to delete the sandbox and will be triggered by the task.
- A new task CLEAN_SANDBOX : this task will run automatically every day at 00:00 and will delete the expired sandboxes.

When setting up a new sanbox, the app will conduct the following steps :

- Create a role with the neccessary privillages to use the newly created sandbox.
- Create a user with a default password 'Password123' that will be requested to change after the first log-in.
- Create a new database for the sandbox.

## Next Relase Features

- Add  the option to delete a sandbox immediatly.
- Provide the option for the user to choose the number of sandbox users.
- Add the possibility to assign user to multiple sandboxes.
- Add a monitor by sandbox and provide the a usage limit by sandbox / sandbox user.
- Upload data to the new created sandbox  (json / csv).
