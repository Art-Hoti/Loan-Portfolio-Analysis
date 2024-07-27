import yaml
from sqlalchemy import create_engine
import pandas as pd

class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.host = credentials['RDS_HOST']
        self.password = credentials['RDS_PASSWORD']
        self.user = credentials['RDS_USER']
        self.database = credentials['RDS_DATABASE']
        self.port = credentials['RDS_PORT']
        self.engine = None

    def init_engine(self):
        self.engine = create_engine(
            f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'
        )

    def extract_data(self):
        if self.engine is None:
            raise Exception("Engine not initialized. Call init_engine() first.")
        query = "SELECT * FROM loan_payments"
        df = pd.read_sql(query, self.engine)
        return df

    def save_data_to_csv(self, df, filename):
        df.to_csv(filename, index=False)

def load_credentials(filepath):
    with open(filepath, 'r') as file:
        credentials = yaml.safe_load(file)
    return credentials

credentials = load_credentials('credentials.yaml')

connector = RDSDatabaseConnector(credentials)

connector.init_engine()
loan_data = connector.extract_data()

csv_filename = 'loan_data.csv'
connector.save_data_to_csv(loan_data, csv_filename)

print(f"Data saved to {csv_filename}")
