from sklearn.preprocessing import OrdinalEncoder
from sklearn.compose import ColumnTransformer
import pandas as pd
import os
from pathlib import Path


class FeatureEngineering:
    def __init__(self):
        self.label = OrdinalEncoder()
        self.train = pd.read_csv("data/raw/train.csv")
        self.test = pd.read_csv("data/raw/test.csv")


        
    def ordinal_encode(self):
 

        trf = ColumnTransformer(
                    transformers=[("label", self.label, [-1])], 
                    remainder="passthrough"
                    )
        
        self.train[" class"] = trf.fit_transform(self.train)
        self.test[' class'] = trf.transform(self.test)
        return self.train , self.test 

    def save_data(self):
        os.makedirs("data/cleaned", exist_ok=True)
        data = self.ordinal_encode()
        data[0].to_csv("data/cleaned/train.csv", index=False)
        data[1].to_csv("data/cleaned/test.csv", index=False)

        