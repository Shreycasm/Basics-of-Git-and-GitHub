from model_trainer  import ModelTrainer


modeltrainer = ModelTrainer()


#training model and predicting  
modeltrainer.train_model()
answer = modeltrainer.predict([1.0,1.0,1.0,1.0,1.0,1.0])

print(answer)
