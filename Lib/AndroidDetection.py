import os
import re
import numpy as np
import json
from Lib.AvgSimForDetect import AvgSimForDetect
from Lib.library import *
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

class AndroidDetection:
    def __init__(self):
        api = open("Res/api_dataset_new_500.json", "r")
        api = json.load(api)
        self.__api_dataset = api
        self.__app_api = load_int_csv('Extract/csv/use500api/12k/app_api.csv')
        self.__invoke = load_int_csv('Extract/csv/use500api/12k/invoke.csv')
        self.__package = load_int_csv('Extract/csv/use500api/12k/package.csv')
        self.__method = load_int_csv('Extract/csv/use500api/12k/method.csv')
        feature_vector = load_float_csv('Extract/csv/use500api/12k/avg_vector.csv')
        label = load_string_csv('Extract/csv/use500api/12k/label.csv')
        model = RandomForestClassifier(n_estimators=100, max_depth=14)
        model.fit(feature_vector, label)
        # model = load_pkl('Extract/pkl/use500api/12k/model.pkl')
        self.__model = model
        

    def create_app_vector(self, data):
        self.__app_api = np.vstack([self.__app_api, app_api([data], self.__api_dataset)])
        avg_sim = AvgSimForDetect(self.__app_api, self.__invoke, self.__package, self.__method)
        feature_vector = create_vector(avg_sim, 1415, 1900, 1911, 2262, 4722)
        return feature_vector

    def predict_raw_data(self, data):
        test_feature_vector = self.create_app_vector(data)
        predict = self.__model.predict(test_feature_vector)
        return {
            "predict": predict[0],
            "vector": test_feature_vector
        }
    
    def predict_app_api(self, data):
        self.__app_api = np.vstack([self.__app_api, [data]])
        avg_sim = AvgSimForDetect(self.__app_api, self.__invoke, self.__package, self.__method)
        feature_vector = create_vector(avg_sim, 2904, 1875, 667, 1307, 1502, 3938)
        predict = self.__model.predict(feature_vector)
        return predict[0]
    
    def predict_feature_vector(self, vector):
        predict = self.__model.predict(vector)
        return predict[0]
