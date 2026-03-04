import joblib
import pandas as pd

MODEL_PATH = "models/predict_freight_model.pkl"

def load_model(model_path:str = MODEL_PATH):
    #load the trained freight cost prediction model 
    with open(model_path,"rb") as f:
        model=joblib.load(f)
    return model

def predict_freight_cost(input_data):
    # predict the freight cost for the input vendors
    # parameters : input_data(dict)
    # output : pd.DataFrame with predicted freight cost
    model=load.model()
    input_df=pd.DataFrame(input_data)
    input_df['Predicted_freight']= model.predict(input_df).round()
    return input_df

if __name__=="__main__":
    # example inference run model testing
    sample_data={"Dollars":[18500,6000,3000,200]}
    prediction=predict_freight_cost(sample_data)
    print(prediction)