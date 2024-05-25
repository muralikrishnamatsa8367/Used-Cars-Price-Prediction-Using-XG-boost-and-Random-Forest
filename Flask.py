from flask import Flask, render_template, request
import joblib
import pandas as pd
from sklearn import preprocessing 

app = Flask(__name__)
label_encoder = preprocessing.LabelEncoder()

@app.route('/')
def index():
    return render_template('index.html', result="")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        car_name_str = request.form['Car_Name']
        present_price = float(request.form['Present_Price'])
        kms_driven = float(request.form['Kms_Driven'])
        fuel_type = int(request.form['Fuel_Type'])
        seller_type = int(request.form['Seller_Type'])
        transmission = int(request.form['Transmission'])
        owner = float(request.form['Owner'])
        age = float(request.form['Age'])
        car_name_numeric = label_encoder.fit_transform([car_name_str])
        print(car_name_numeric)
        data_new = pd.DataFrame({
            'Car_Name': car_name_numeric,
            'Present_Price': present_price,
            'Kms_Driven': kms_driven,
            'Fuel_Type': fuel_type,
            'Seller_Type': seller_type,
            'Transmission': transmission,
            'Owner': owner,
            'Age': age
        }, index=[0])

        model = joblib.load('car_price_predictor')

        result = model.predict(data_new)

        return render_template('index.html', result=f"Car Purchase amount: {result[0]}")

    except Exception as e:
        return render_template('index.html', result=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
