import snowflake.connector



class snowcon:
    def __init__(self, username, password, account, warhouse, role) -> None:
        self.username = username
        self.password = password
        self.account = account
        self.warhouse = warhouse
        self.role = role

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
        return self.check_function("SHOW ROLES LIKE 'SANDBOX_ROLE';")

    def check_creation_procedure(self):
        return self.check_function("SHOW PROCEDURES  LIKE 'SANDBOX_CREATE' IN DATABASE 'SANDBOX_MAIN';")

    
    def check_cleaning_procedure(self):
        return self.check_function("SHOW ROLES LIKE 'SANDBOX_DROP' IN DATABASE 'SANDBOX_MAIN';")

    def check_task(self):
        return self.check_function("SHOW TASKS LIKE 'SANDBOX_DROP'  IN DATABASE 'SANDBOX_MAIN';")

    
    def check_database(self):
        return self.check_function("SHOW DATABASES LIKE 'SANDBOX_MAIN';")
        
    
    def check_log_table(self):
        return self.check_function("SHOW TABLES LIKE 'SANDBOX_LOG';")
        
            
    def check_warhouse(self):
        return self.check_function("SHOW WAREHOUSES LIKE 'SANDBOX_WH'; ")
        
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
        return True, None
    
    def create_cleaning_procedure(self):
        return True, None
    
    def create_task(self):
        return True, None
    
    def create_user(self):
        return True, None

    def create_role(self):
        return True, None


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
    def run_procedure(self):
        pass
#####################################################################################################

def validated_credentials(username, password, account, warhouse, role):
    try:
        cnx = snowflake.connector.connect(
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

