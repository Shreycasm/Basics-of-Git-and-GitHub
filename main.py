from data_collection import DataCollection 
from feature_engineering import FeatureEngineering
from model_trainer  import ModelTrainer





datacollection = DataCollection()
featureengineering = FeatureEngineering()
modeltrainer = ModelTrainer()


#fetching data from databse and saving locally
datacollection.save_data()

#cleaning data and saving locally
featureengineering.save_data()


#training model and predicting  
modeltrainer.train_model()
answer = modeltrainer.predict([1.0,1.0,1.0,1.0,1.0,1.0])

print(answer)
