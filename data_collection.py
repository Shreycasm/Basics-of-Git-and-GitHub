import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from sklearn.model_selection import train_test_split

load_dotenv()

class DataCollection:
    def __init__(self):
        self.user = os.getenv("USER")
        self.password = os.getenv("PASSWORD")
        self.host = os.getenv("HOST")
        self.database = os.getenv("DATABASE_NAME")
        self.tablename = os.getenv("TABLE_NAME")
        self.engine = create_engine(f"mysql+mysqlconnector://{self.user}:{self.password}@{self.host}/{self.database}").connect()

    def get_data(self):
        return pd.read_sql_query(f"SELECT * FROM {self.tablename}", self.engine)
    
    def split_data(self):
        data = self.get_data()
        train, test = train_test_split(data, test_size=0.2, random_state=42)
        return train, test

    def save_data(self):
        os.makedirs("data/raw", exist_ok=True)
        self.get_data().to_csv("data/raw/raw_data.csv", index=False)
        self.split_data()[0].to_csv("data/raw/train.csv", index=False)
        self.split_data()[1].to_csv("data/raw/test.csv", index=False)