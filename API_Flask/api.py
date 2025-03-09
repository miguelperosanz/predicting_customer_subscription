from flask import Flask, request, jsonify
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "welcome to Miguel's api"


@app.route('/prediction', methods=['GET'])
def prediction():

    # loading the model
    with open('API_Flask/model/optimized_xgboost.pkl', "rb") as file:
        loaded_model = pickle.load(file)

    # defining the dictionary
    data = {
            "age" : request.args.get('age'),
            "job" : request.args.get('job'),
            "marital" : request.args.get('marital'),
            "education" : request.args.get('education'),
            "default" : request.args.get('default'),
            "housing" : request.args.get('housing'),
            "loan" : request.args.get('loan'),
            "contact" : request.args.get('contact'),
            "month" : request.args.get('month'),
            "dayweek" : request.args.get('dayweek'),
            "duration" : request.args.get('duration'),
            "campaign" : request.args.get('campaign'),
            "previous" : request.args.get('previous'),
            "poutcome" : request.args.get('poutcome'),
             }   
     
    
    df = pd.DataFrame([data])

    # loading the scaler
    with open("API_Flask/scaler/scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
    df[['age','campaign']] = scaler.transform(df[['age','campaign']])

    # preparing the dataframe in the proper format to be ingested by the model for inferencing:
    features_list = df.values.tolist()
    features_list = [[float(x) if '.' in str(x) else int(x) for x in row] for row in features_list]  # Converting strings to integers (if they exist)

    prediction = loaded_model.predict(features_list)
    probabilities = loaded_model.predict_proba(features_list)
    predicted_probs = (probabilities[:, 1] * 100).round(1)

    # example of url:
    # http://127.0.0.1:5000/prediction?age=34&job=1&marital=2&education=1&default=0&housing=0&loan=0&contact=0&month=2&dayweek=2&duration=2&campaign=1&previous=0&poutcome=1

    # Return a message based on the parameters
    return jsonify({
        "prediction": int(prediction),
        "probability of customer buying (%)": round(float(predicted_probs[0]), 1) 
        })

if __name__ == "__main__":
    app.run(debug=True)
    