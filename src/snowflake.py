import snowflake.connector


def connection(username, password, account, warhouse, role):
    return snowflake.connector.connect(
        user=username,
        password=password,
        account=account,
        warehouse=warhouse,
        role=role
        )

def validated_credentials(username, password, account, warhouse, role):
    try:
        connection(username, password, account, warhouse, role)
        return True 
    except Exception as e :
        print(e)
        return False