-- CREATE THE MASTER DATABASE WHICH WILL CONTAINS ALL THE OBJECTS 
CREATE DATABASE IF NOT EXISTS SANDBOX_MAIN;

-- CREATE THE LOG TABLE WHICH WILL SAVE THE SANBOXES
CREATE TABLE IF NOT EXISTS SANDBOX_MAIN.PUBLIC.SANDBOX_LOG(
    USER_NAME VARCHAR,
    EXPIRATION_DATE date, 
    CREATION_DATE date
  ) ;

-- CREATE THE ROLE WHICH WILL MONITOR THE SANDBOXES AND HAVE ACCESS TO ALL OF THEM 
CREATE ROLE  IF NOT EXISTS  SANDBOX_ROLE  ; 

-- CREATE A DEFAULT USER FOR THE SANDBOX_ROLE  ( DEFAULT PASSWORD = Password123 )
CREATE  USER  IF NOT EXISTS SANDBOX_MONITOR
password='Password123'
default_role = SANDBOX_ROLE
must_change_password = true 
COMMENT = "This user can be used to monitor sandboxes" ; 