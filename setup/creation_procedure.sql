BEGIN
CREATE OR REPLACE PROCEDURE SANDBOX_MAIN.PUBLIC.SANBOX_SETUP("USER_NAME" VARCHAR, "EXPIRY_DATE" DATE)
RETURNS VARCHAR
LANGUAGE SQL
COMMENT='This procedure create a fresh environment for the sanbox_user'
EXECUTE AS CALLER
AS 
declare
  DATABASE_NAME string default UPPER($$SANDBOX_DB_$$||:USER_NAME);
  ROLE_NAME string default UPPER($$SANDBOX_ROLE_$$||:USER_NAME);
  WAREHOUSE_NAME string default UPPER($$SANDBOX_WH_$$||:USER_NAME) ;
begin
  
  -- create the database
  CREATE OR REPLACE DATABASE identifier(:DATABASE_NAME) ; 

  USE DATABASE identifier(:DATABASE_NAME) ; 

  -- create the canddidat role 
  CREATE ROLE  IF NOT EXISTS  identifier(:ROLE_NAME)  ; 
  
  -- create warhouse for the sanbox_user 
  CREATE OR REPLACE WAREHOUSE identifier(:WAREHOUSE_NAME)    
  WAREHOUSE_SIZE  = XSMALL
  INITIALLY_SUSPENDED = TRUE
  COMMENT = "This warehouse will be used by the sanbox_user"  ; 
  
  -- create the sanbox_user user 
  CREATE  USER  IF NOT EXISTS identifier(:USER_NAME) 
  password=$$Password123$$
  default_role = :ROLE_NAME
  must_change_password = true 
  COMMENT = "This user is dedicated for the sanbox_user" ; 

  -- create and grant the privillage to the sanbox_user role 
  CREATE ROLE IF NOT EXISTS identifier(:ROLE_NAME)  ; 
  GRANT ROLE identifier(:ROLE_NAME)  TO  USER identifier(:USER_NAME);  
  GRANT ALL ON DATABASE identifier(:DATABASE_NAME)  TO ROLE  identifier(:ROLE_NAME) ;

  GRANT ALL ON SCHEMA PUBLIC  TO ROLE  identifier(:ROLE_NAME) ;
  GRANT USAGE ON WAREHOUSE identifier(:WAREHOUSE_NAME) TO ROLE identifier(:ROLE_NAME);
 
  --create and grant the privillage to the SANDBOX_MONITOR role 
  GRANT ROLE identifier(:ROLE_NAME) TO ROLE SANDBOX_MONITOR_ROLE ;

  --insert the informations of the added BEWERBER into the table INFROMATION_BEWERBER
  INSERT INTO SANDBOX_MAIN.PUBLIC.SANDBOX_LOG (USER_NAME, EXPIRATION_DATE, CREATION_DATE) values (:USER_NAME, :EXPIRY_DATE, CURRENT_DATE()) ;
  
  return '=> ENVIRONMENT CREATED SUCCESSFULLY' ;
END;
END;
