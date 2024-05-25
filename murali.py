#LABEL ENCODING
#Convert the categorical values into numerical values (car names )
data = pd.read_csv('carproject.csv')
from sklearn import preprocessing 
label_encoder = preprocessing.LabelEncoder()
data['Car_Name'] = label_encoder.fit_transform(data['Car_Name'])
#Reamining values
data['Fuel_Type'] = data['Fuel_Type'].map({'Petrol':0,'Diesel':1,'CNG':2})
data['Seller_Type'] = data['Seller_Type'].map({'Dealer':0,'Individual':1})
data['Transmission'] =data['Transmission'].map({'Manual':0,'Automatic':1})
#store independent variables in x
#store target varibale in y
X = data.drop(['Selling_Price'],axis=1)
y = data['Selling_Price']
#model training
lr = LinearRegression()
lr.fit(X_train,y_train)

rf = RandomForestRegressor()
rf.fit(X_train,y_train)

xgb = GradientBoostingRegressor()
xgb.fit(X_train,y_train)

xg = XGBRegressor()
xg.fit(X_train,y_train)
#scores of models
	Models	R2_SCORE
0	LR	0.677357
1	RF	0.766606
2	GBR	0.873460
3	XG	0.920530
#save the model
joblib.dump(xg_final,'car_price_predictor')
#prediction on data
data_new = pd.DataFrame({
    'Car_Name':90,
    'Present_Price':5.59,
    'Kms_Driven':27000,
    'Fuel_Type':0,
    'Seller_Type':0,
    'Transmission':0,
    'Owner':0,
    'Age':8
},index=[0])
model.predict(data_new)