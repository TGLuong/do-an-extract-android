from pickle import load
import re
import pandas as pd
import numpy as np
from Lib.library import *
from Lib.AvgSim import AvgSim
from Lib.Path import Path
import json
from Lib.AndroidDetection import AndroidDetection


def extract_data():
    api_dataset_file = open("Res/api_dataset_new_500.json", "r")
    api_dataset = json.load(api_dataset_file)
    data = get_apis('D:\\TTCSCN', api_dataset = api_dataset)
    data = json.dumps(data, indent = 4)
    out_file = open("Extract/new_train_11k/benign.json", 'w')
    out_file.write(data)
    out_file.close()

def create_base_matrix():
    api_dataset_file = open("Res/api_dataset_new_500.json", "r")
    api_dataset = json.load(api_dataset_file)
    data_file = open("Extract/new_train_11k/training_11k.json", "r")
    data = json.load(data_file)
    print("app_api")
    save_int_csv("Extract/csv/use500api/12k/app_api.csv", app_api(data, api_dataset))
    print("label")
    save_string_csv("Extract/csv/use500api/12k/Label.csv", label(extract_data = data))
    print("invoke")
    save_int_csv("Extract/csv/use500api/12k/invoke.csv", invoke(data, api_dataset))
    print("package")
    save_int_csv("Extract/csv/use500api/12k/package.csv", package(api_dataset))
    print("method")
    save_int_csv("Extract/csv/use500api/12k/method.csv", method(data, api_dataset))

def create_avgsim():
    base_dir = 'Extract/csv/5000app/'
    app_api = pd.read_csv(base_dir + "app_api.csv", index_col=0, header=0)
    app_api = app_api.loc[:, app_api.columns != "Label"]
    app_api = app_api.to_numpy()
    invoke = pd.read_csv(base_dir + "invoke.csv", index_col=0, header=0).to_numpy()
    package = pd.read_csv(base_dir + "package.csv", index_col=0, header=0).to_numpy()
    method = pd.read_csv(base_dir + "method_pd.csv", index_col=0, header=0).to_numpy()

    agvSim = Path(app_api, invoke, package, method)

    save_folder = base_dir + "path"

    print("m1")
    save_int_csv(f"{save_folder}/m1.csv", agvSim.meta_path_1())
    print("m2")
    save_int_csv(f"{save_folder}/m2.csv", agvSim.meta_path_2())
    print("m3")
    save_int_csv(f"{save_folder}/m3.csv", agvSim.meta_path_3())
    print("m4")
    save_int_csv(f"{save_folder}/m4.csv", agvSim.meta_path_4())
    return
    print("m5")
    save_int_csv(f"{save_folder}/m5.csv", agvSim.meta_path_5())
    print("m6")
    save_int_csv(f"{save_folder}/m6.csv", agvSim.meta_path_6())
    print("m7")
    save_int_csv(f"{save_folder}/m7.csv", agvSim.meta_path_7())
    print("m8")
    save_int_csv(f"{save_folder}/m8.csv", agvSim.meta_path_8())
    print("m9")
    save_int_csv(f"{save_folder}/m9.csv", agvSim.meta_path_9())
    print("m10")
    save_int_csv(f"{save_folder}/m10.csv", agvSim.meta_path_10())
    print("m11")
    save_int_csv(f"{save_folder}/m11.csv", agvSim.meta_path_11())
    print("m12")
    save_int_csv(f"{save_folder}/m12.csv", agvSim.meta_path_12())
    print("m13")
    save_int_csv(f"{save_folder}/m13.csv", agvSim.meta_path_13())
    print("m14")
    save_int_csv(f"{save_folder}/m14.csv", agvSim.meta_path_14())
    print("m15")
    save_int_csv(f"{save_folder}/m15.csv", agvSim.meta_path_15())
    print("m16")
    save_int_csv(f"{save_folder}/m16.csv", agvSim.meta_path_16())
    
def create_diminutive():
    base_dir = 'Extract/csv/5000app/'
    app_api = pd.read_csv(base_dir + "app_api.csv", index_col=0, header=0)
    app_api = app_api.loc[:, app_api.columns != "Label"]
    app_api = app_api.to_numpy()
    invoke = pd.read_csv(base_dir + "invoke.csv", index_col=0, header=0).to_numpy()
    package = pd.read_csv(base_dir + "package.csv", index_col=0, header=0).to_numpy()
    method = pd.read_csv(base_dir + "method_pd.csv", index_col=0, header=0).to_numpy()

    save_folder = base_dir + "path"

    print("diminutive_1")
    diminutive_1 = app_api.T
    save_int_csv(f"{save_folder}/diminutive_m1.csv", diminutive_1)

    print("diminutive 2")
    diminutive_2 = method @ app_api.T
    save_int_csv(f"{save_folder}/diminutive_m2.csv", diminutive_2)

    print("diminutive 3")
    diminutive_3 = package @ app_api.T
    save_int_csv(f"{save_folder}/diminutive_m3.csv", diminutive_3)

    print("diminutive 4")
    diminutive_4 = invoke @ app_api.T
    save_int_csv(f"{save_folder}/diminutive_m4.csv", diminutive_4)
    ...

def feature_vector():
    paths = [
        './Extract/csv/use500api/12k/AvgSim/m1.csv',
        './Extract/csv/use500api/12k/AvgSim/m2.csv',
        './Extract/csv/use500api/12k/AvgSim/m3.csv',
        './Extract/csv/use500api/12k/AvgSim/m4.csv',
        './Extract/csv/use500api/12k/AvgSim/m5.csv',
        './Extract/csv/use500api/12k/AvgSim/m6.csv',
        './Extract/csv/use500api/12k/AvgSim/m7.csv',
        './Extract/csv/use500api/12k/AvgSim/m8.csv',
        './Extract/csv/use500api/12k/AvgSim/m9.csv',
        './Extract/csv/use500api/12k/AvgSim/m10.csv',
        './Extract/csv/use500api/12k/AvgSim/m11.csv',
        './Extract/csv/use500api/12k/AvgSim/m12.csv',
        './Extract/csv/use500api/12k/AvgSim/m13.csv',
        './Extract/csv/use500api/12k/AvgSim/m14.csv',
        './Extract/csv/use500api/12k/AvgSim/m15.csv',
        './Extract/csv/use500api/12k/AvgSim/m16.csv'
    ]
    data = create_feature_vector_5_label(paths, 1415, 1900, 1911, 2262, 4722)
    save_float_csv("Extract/csv/use500api/12k/avg_vector.csv", data)
    
def attach_label():
    none_label = open("Extract/data_extract_prev.json", "r")
    datas = json.load(none_label)
    for i, data in enumerate(datas):
        android = AndroidDetection()
        datas[i]["label"] = android.predict_raw_data(data)
    result = open("Extract/data_extract_prev_v2.json", "w")
    result.write(json.dumps(datas, indent=4))
    result.close()

    return

def sorter1(app):
    label = app["label"]
    if(label == "benign"):
        return 1
    elif(label == "adware"):
        return 2
    elif(label == "botnet"):
        return 3
    elif(label == "ransomeware"):
        return 4
    elif(label == "scareware"):
        return 5
    elif(label == "smsmalware"):
        return 6

def sorter2(label):
    if(label == "benign"):
        return 1
    elif(label == "adware"):
        return 2
    elif(label == "botnet"):
        return 3
    elif(label == "ransomeware"):
        return 4
    elif(label == "scareware"):
        return 5
    elif(label == "smsmalware"):
        return 6

def sort():
    datas = open("Extract/data_extract_prev_join.json", "r")
    datas = json.load(datas)
    datas = sorted(datas, key = sorter1)
    file = open("Extract/data_extract_prev_sorted.json", "w")
    file.write(json.dumps(datas, indent=4))
    file.close()
    return

def attach_label_12000():
    app_apis = load_pkl("Res/12000/app_api.pkl")
    result = []
    for app in app_apis:
        android = AndroidDetection()
        result.append(android.predict_app_api(app))
    save_int_csv("Extract/csv/Avg12000/app_api.csv", app_apis)
    save_string_csv("Extract/csv/Avg12000/label.csv", result)
    return

def convert_to_csv_12000():
    invoke = load_pkl("Res/12000/invoke.pkl")
    method = load_pkl("Res/12000/method.pkl")
    package = load_pkl("Res/12000/package.pkl")
    save_int_csv("Extract/csv/Avg12000/invoke.csv", invoke)
    save_int_csv("Extract/csv/Avg12000/method.csv", method)
    save_int_csv("Extract/csv/Avg12000/package.csv", package)
    return

def sort12000():
    app_api = load_int_csv("Extract/csv/Avg12000/app_api.csv")
    label = load_string_csv("Extract/csv/Avg12000/label.csv")
    app_api = app_api.tolist()
    for i in range(0, len(label) - 1):
        for j in range(i+1, len(label)):
            if sorter2(label[i]) > sorter2(label[j]):
                temp = app_api[i]
                app_api[i] = app_api[j]
                app_api[j] = temp
                temp = label[i]
                label[i] = label[j]
                label[j] = temp
    save_int_csv("Extract/csv/Avg12000/app_api_sort.csv", app_api)
    save_string_csv("Extract/csv/Avg12000/label_sort.csv", label)
    return

def to_pkl():
    app_api = load_int_csv("Extract/csv/use500api/12k/app_api.csv")
    invoke = load_int_csv("Extract/csv/use500api/12k/invoke.csv")
    package = load_int_csv("Extract/csv/use500api/12k/package.csv")
    method = load_int_csv("Extract/csv/use500api/12k/method.csv")

    save_pkl("Extract/pkl/use500api/12k/app_api.pkl", app_api)
    save_pkl("Extract/pkl/use500api/12k/invoke.pkl", invoke)
    save_pkl("Extract/pkl/use500api/12k/package.pkl", package)
    save_pkl("Extract/pkl/use500api/12k/method.pkl", method)


if __name__ == "__main__":
    create_diminutive()