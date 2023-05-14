from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
import numpy as np




def ml_function(odometer, year, model_name):
    cars_df = pd.read_csv(Path("ml_model/used_cars_data.csv"), parse_dates=True, infer_datetime_format=True)
    cars_df = cars_df[['mileage','year','model_name','price']]
    cars_df.dropna(inplace=True)
    categorical_variables = list(cars_df.dtypes[cars_df.dtypes == "object"].index)
    enc = OneHotEncoder(sparse=False, handle_unknown='ignore')
    encoded_data = enc.fit_transform(cars_df[categorical_variables])
    encoded_df = pd.DataFrame(encoded_data,columns = enc.get_feature_names_out(categorical_variables))
    numerical_variables_df = cars_df.drop(columns = categorical_variables)
    carscleaned_df = pd.concat([numerical_variables_df,encoded_df],axis=1)
    model = XGBRegressor()
    X = carscleaned_df.drop(['price'],axis=1)
    y = carscleaned_df['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
    scaler = StandardScaler()
    X_scaler = scaler.fit(X_train)
    X_train_scaled = X_scaler.transform(X_train)
    X_test_scaled = X_scaler.transform(X_test)
    model.fit(X_train_scaled, y_train)

    data = {'mileage': odometer, 'year': year, 'model_name': model_name}
    df = pd.DataFrame(data,index=[0])
    new_encoded_data = enc.transform(df[categorical_variables])
    encoded_df = pd.DataFrame(new_encoded_data,columns = enc.get_feature_names_out(categorical_variables))
    new_numerical_variables_df = df.drop(columns = categorical_variables)
    new_carscleaned_df = pd.concat([new_numerical_variables_df,encoded_df],axis=1)
    input_test_scaled = X_scaler.transform(new_carscleaned_df)
    prediction = model.predict(input_test_scaled)
    formatted_prediction = "The estimated selling price of your car is ${:,.0f}".format(prediction[0])
    return formatted_prediction