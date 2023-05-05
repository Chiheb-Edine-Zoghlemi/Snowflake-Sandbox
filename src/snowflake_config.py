import snowflake.connector
import os 
import re 
snowflake.connector.paramstyle = 'qmark'

class snowcon:
    def __init__(self, username, password, account, warhouse) -> None:
        self.username = username
        self.password = password
        self.account = account
        self.warhouse = warhouse

    def connection(self):
        return snowflake.connector.connect(
            user=self.username,
            password=self.password,
            account=self.account,
            warehouse=self.warhouse,
            role=self.role
            )
#####################################################################################################
#                           SYSTEM OBJECTS CHECKING
#####################################################################################################
    def check_function(self, query):
        with  self.connection().cursor() as cs:
                try:
                    cs.execute(query)
                    if cs.fetchone():
                        return True
                except Exception as e :
                    print("[ CHECKING FUNCTION ERROR ]",e)
                    return False

    def check_user(self):
        return self.check_function("SHOW USERS LIKE 'SANDBOX_MONITOR';")
        

    def check_role(self):
        return self.check_function("SHOW ROLES LIKE 'SANDBOX_MONITOR_ROLE';")

    def check_creation_procedure(self):
        return self.check_function("SHOW PROCEDURES  LIKE 'SANBOX_SETUP' IN DATABASE SANDBOX_MAIN;")

    
    def check_cleaning_procedure(self):
        return self.check_function("SHOW PROCEDURES LIKE 'SANDBOX_DROP' IN DATABASE SANDBOX_MAIN ;")

    def check_task(self):
        return self.check_function("SHOW TASKS LIKE 'CLEAN_SANDBOX'  IN DATABASE SANDBOX_MAIN;")

    
    def check_database(self):
        return self.check_function("SHOW DATABASES LIKE 'SANDBOX_MAIN';")
        
    
    def check_log_table(self):
        return self.check_function("SHOW TABLES LIKE 'SANDBOX_LOG' IN DATABASE SANDBOX_MAIN ; ")
        
            
    def check_warhouse(self):
        return self.check_function("SHOW WAREHOUSES LIKE 'SANDBOX_MONITOR_WH' ; ")
    
  
        
#####################################################################################################
#                           SYSTEM OBJECT CREATION
#####################################################################################################
    def creation_function(self, query):
        with  self.connection().cursor() as cs:
                try:
                    cs.execute(query)
                    return True, None
                except Exception as e :
                    print("[ CREATION FUNCTION ERROR ]",e)
                    return False, e

    def create_creation_procedure(self):
        with open(os.path.join('setup','creation_procedure.sql'),mode='r') as file :
            sql_script = file.read().strip()
        return self.creation_function(sql_script)
    
    def create_cleaning_procedure(self):
        with open(os.path.join('setup','clean_procedure.sql'),mode='r') as file :
            sql_script = file.read().strip()
        return self.creation_function(sql_script)
    
    def create_task(self):
        return self.creation_function("""
        BEGIN
        CREATE TASK  IF NOT EXISTS SANDBOX_MAIN.PUBLIC.CLEAN_SANDBOX
        warehouse = SANDBOX_MONITOR_WH
        schedule = 'USING CRON  0 0 * * * UTC'
        as
        call SANDBOX_MAIN.PUBLIC.SANDBOX_DROP() ;
        ALTER task SANDBOX_MAIN.PUBLIC.CLEAN_SANDBOX resume;
        END ; 
        """)
    
    def create_user(self):
        return self.creation_function(""" 
        CREATE  USER  IF NOT EXISTS SANDBOX_MONITOR
        password=$$Sanddbox_monitor123$$
        default_role = SANDBOX_ROLE
        must_change_password = true 
        COMMENT = "This user is dedicated for the sandbox monitor" ; """)

    def create_role(self):
        return self.creation_function(f""" 
        BEGIN
        CREATE ROLE  IF NOT EXISTS  SANDBOX_MONITOR_ROLE  ;  
        GRANT ROLE SANDBOX_MONITOR_ROLE TO ROLE SYSADMIN ;
        GRANT ROLE SANDBOX_MONITOR_ROLE TO USER SANDBOX_MONITOR ;
        END;
        """)


    def create_warehouse(self):
        return self.creation_function(""" 
        CREATE OR REPLACE WAREHOUSE SANDBOX_MONITOR_WH    
        WAREHOUSE_SIZE  = XSMALL
        INITIALLY_SUSPENDED = TRUE
        COMMENT = "This warehouse will be used by the sandbox monitor user"  ; """)


    def create_database(self):
        return self.creation_function("CREATE DATABASE IF NOT EXISTS SANDBOX_MAIN;")
       

    def create_log_table(self):
        return self.creation_function("""CREATE TABLE IF NOT EXISTS SANDBOX_MAIN.PUBLIC.SANDBOX_LOG(
            USER_NAME VARCHAR,
            EXPIRATION_DATE date, 
            CREATION_DATE date) ;""")
       

#####################################################################################################
    def load_sandboxes(self):
        records = []
        with  self.connection().cursor() as cs:
            cs.execute("SELECT USER_NAME, EXPIRATION_DATE, CREATION_DATE from SANDBOX_MAIN.PUBLIC.SANDBOX_LOG ")
            records  = cs.fetchall()
        return records
    
    def run_procedure(self, user_name, expiry_date, uploaded_files):
        try:
            with  self.connection().cursor() as cs:
                cs.execute("CALL SANDBOX_MAIN.PUBLIC.SANBOX_SETUP(?, ?)",[re.sub(' +', ' ', user_name).replace(' ','_'), expiry_date])
            return  True 
        except Exception as e :
            print(f' [ ERROR CREATING SANDBOX ] : {e}')
            return False
            
# INSERT INTO varia (v) SELECT TO_VARIANT(PARSE_JSON('{"key3": "value3", "key4": "value4"}'));
# CREATE TABLE varia (v VARIANT);
#####################################################################################################

def validated_credentials(username, password, account, warhouse, role):
    try:
        snowflake.connector.connect(
            user=username,
            password=password,
            account=account,
            warehouse=warhouse,
            role=role
            )
        return True 
    except Exception as e :
        print(e)
        return False

