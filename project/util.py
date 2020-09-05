import pandas as pd
import numpy as np
import json
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import json
sc = StandardScaler()

__locations = None
__data_columns = None
__model = None

df = pd.read_csv("project/artifacts/one_hot_data.csv")

# Split data
X = df.drop('price', axis=1)
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=51)

# feature scaling
sc = StandardScaler()
sc.fit(X_train)
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)

""" Routine that uses the model to return the estimated prices"""
def get_estimated_price(location,sqft,bhk,bath, is_ready):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = bhk
    x[1] = sqft
    x[2] = bath
    if loc_index >= 0:
        x[loc_index] = 1
    x = sc.transform([x])[0]
    return round(__model.predict([x])[0], 2)

"""Load the following: 
        1. Model : __model
        2. Columns :__data_columns"""
def load_save_artifacts():
    # print("loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("project/artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[4:]  # first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        __model = joblib.load('project/artifacts/bangalore_house_prices_joblib.pkl')
    # print("loading saved artifacts...done")
    # print(__locations)


def get_location_names():
    return __locations


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_save_artifacts()
    # print(get_location_names())
    # print(get_estimated_price('1st Phase JP Nagar',3000, 3, 3,1))
    # print(get_estimated_price('1st Phase JP Nagar', 2500, 2, 2,1))
    # print(get_estimated_price('Kalhalli', 1000, 2, 2,1)) # other location
    # print(get_estimated_price('Ejipura', 2000, 2, 2,1))  # other location