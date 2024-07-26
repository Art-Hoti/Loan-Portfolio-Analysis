# db_utils.py

import pymysql  

class RDSDatabaseConnector:
    """
    A class to connect to an RDS database and extract loan payment data.
    """

    def __init__(self, host, user, password, database):
        """
        Initialize the RDSDatabaseConnector with database connection parameters.

        :param host: The hostname or IP address of the database server.
        :param user: The username for the database connection.
        :param password: The password for the database user.
        :param database: The name of the database to connect to.
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        """
        Establish a connection to the RDS database.
        """
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Connection to the database was successful.")
        except pymysql.MySQLError as e:
            print(f"Error connecting to the database: {e}")
            self.connection = None

    def disconnect(self):
        """
        Close the connection to the RDS database.
        """
        if self.connection:
            self.connection.close()
            print("Disconnected from the database.")
