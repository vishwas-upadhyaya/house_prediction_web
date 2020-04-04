import json
import numpy as np
import pickle
columns=None
def get_all_locations():
    global columns
    with open('prediction/columns.json','r') as f:
        cols=json.load(f)['data_columns']
        columns=cols
        col=cols[3:]
        return col

def get_estimated_price(location,sqft,bhk,bath):
    global columns
    with open('prediction/banglore_price_predict_model.pickle','rb') as f:
        lr_clf=pickle.load(f)
    #columns=get_all_locations()
    print(len(columns),columns)
    loc_index = columns.index(location.lower())
    print(loc_index)
    X = np.zeros(len(columns))
    X[0] = sqft
    X[1] = bath
    X[2] = bhk
    if loc_index >= 0:
        X[loc_index] = 1
    return round(lr_clf.predict([X])[0],2)


