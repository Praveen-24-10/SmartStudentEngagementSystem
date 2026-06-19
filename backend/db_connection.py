import oracledb

def get_connection():

    connection = oracledb.connect(
        user="SYSTEM",
        password="YOUR_PASSWORD",
        host="localhost",
        port=1521,
        service_name="XEPDB1"
    )

    return connection