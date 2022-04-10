from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
model = load_model("houseprice.h5")

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():

    Bedrooms = request.form["Bedrooms"]
    Bathrooms = request.form["Bathrooms"]
    Sqft_Living = request.form["Sqft_Living"]
    Sqft_Lot = request.form["Sqft_Lot"]
    Floors = request.form["Floors"]
    Waterfront = request.form["Waterfront"]
    View = request.form["View"]
    Condition = request.form["Condition"]
    Sqft_Above = request.form["Sqft_Above"]
    Sqft_Basement = request.form["Sqft_Basement"]
    Yr_Built = request.form["Yr_Built"]
    Yr_Renovated = request.form["Yr_Renovated"]
    Lat = request.form["Lat"]
    Long = request.form["Long"]    
    Sqft_Living15 = request.form["Sqft_Living15"]   
    Sqft_Lot15 = request.form["Sqft_Lot15"]

    
    

#     arr = np.array([Bathrooms,Bedrooms,Condition,Floors,Lat,Long,Sqft_Above,Sqft_Basement,Sqft_Living,Sqft_Living15,Sqft_Lot,Sqft_Lot15,View,
# Yr_Built,Yr_Renovated])
    # df = pd.DataFrame({"Bathrooms" : Bathrooms,"Bedrooms" : Bedrooms ,"Sqft_Living": Sqft_Living,"Sqft_Lot" :Sqft_Lot,"Floors" : Floors,"Waterfront":Waterfront,"View" :View,"Condition" : Condition, "Sqft_Above" :Sqft_Above,"Sqft_Basement" :Sqft_Basement,"Yr_Built" : Yr_Built,"Yr_Renovated" : Yr_Renovated, "Lat" : Lat,"Long" :Long,"Sqft_Living15" :Sqft_Living15, "Sqft_Lot15" :Sqft_Lot15})

    # df = np.array([Bathrooms,Bedrooms,Sqft_Living,Sqft_Lot,Floors,Waterfront,View,Condition,Sqft_Above,Sqft_Basement,Yr_Built,Yr_Renovated,Lat,Long,Sqft_Living15,Sqft_Lot15])
    # df = df.astype(np.float64)
    s_scaler = StandardScaler()
    # print("data idher hai ",df)
    # single_house = s_scaler.transform(df.reshape(-1,16))
    # print("data mein loacha hai ", single_house)

    arr = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) 
    single_house = s_scaler.transform(arr.reshape(-1,16))
    y_pred = model.predict(single_house)
    print(y_pred)
    # prediction = model.predict(single_house)
  
    # return render_template('index.html', Predict_score ='Your house estimate price is  ₹ {} lakhs'.format(prediction))

if __name__ == "__main__":
    app.run(debug=True)
