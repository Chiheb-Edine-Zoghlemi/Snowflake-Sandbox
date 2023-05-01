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

    def check_user(self):
        return False

    def check_role(self):
        return True

    def check_database(self):
        return True

    def check_warhouse(self):
        return False

    def load_test(self):
        records = []
        with  self.connection().cursor() as cs:
            cs.execute("SELECT USER_NAME, EXPIRATION_DATE, CREATION_DATE from MDWH_ASSESSMENTTEST_MASTER.PUBLIC.INFROMATION_BEWERBER ")
            records  = cs.fetchall()
        return records


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
        return False

