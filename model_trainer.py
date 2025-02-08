from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

class ModelTrainer:
    def __init__(self):
        self.model = RandomForestClassifier()
        self.train = pd.read_csv("data/cleaned/train.csv")
        self.train.columns = self.train.columns.str.strip()
        self.X_train = self.train.drop(columns=["class"])
        self.y_train = self.train["class"]
        self.columns = self.X_train.columns

    def train_model(self):
        self.model.fit(self.X_train, self.y_train)

    def predict(self, data):
        data = pd.DataFrame(np.array(data).reshape(1, -1), columns=self.columns)
        label =  self.model.predict(data)

        if label[0] == 1:
            return "Non Bankruptcy"
        else:
            return "Bankruptcy"
