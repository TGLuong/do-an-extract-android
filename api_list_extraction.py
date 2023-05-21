import os
from typing import OrderedDict
from Lib.library import *
from collections import Counter
import json
def extract_apis_names(path, data = None):
    """
    extract api of android app
    @param[in] path : path of android app
    @param[in] api_dataset : list of api is extracted in anroid app
    @param[in] label : the label is set to the file
    return 
    """
    if (data == None): data = set()
    for smaliFile in list_smali_file(path):
        try:
            file_content = open(smaliFile, 'r').readlines()
            api_found = False
            for row in file_content:
                if re.match(r'^.method', row):
                    api_found = True
                    continue
                if (api_found == True):
                    row = row.strip()
                    if re.search(r'^invoke', row):
                        a = API(row)
                        if ((a.api.find("Landroid") != -1) or (a.api.find("Ljava") != -1)):
                            data.add(a.api)
                else:
                    continue
                if re.match(r'^.end method', row):
                    api_found = False
        except:
            pass
    os.system('rmdir /s /q \"{}\"'.format(path))
    return data

def get_list_malicious_apis(path, data_malware = None):

    if data_malware == None:
        data_malware = dict()
    
    data_benign = dict()

    path_benign = path + '/Benign/'
    path_adware = path + '/Adware/'
    path_botnet = path + '/Botnet/'
    path_ransomware = path + '/Ransomware/'
    path_scareware = path + '/Scareware/'
    path_smsmalware = path + '/SMSmalware/'

    list_benign = [path_benign + f for f in os.listdir(path_benign)]
    list_adware = [path_adware + f for f in os.listdir(path_adware)]
    list_botnet = [path_botnet + f for f in os.listdir(path_botnet)]
    list_ransomware = [path_ransomware + f for f in os.listdir(path_ransomware)]
    list_scareware = [path_scareware + f for f in os.listdir(path_scareware)]
    list_smsmalware = [path_smsmalware + f for f in os.listdir(path_smsmalware)]
    
    for i, file in enumerate(list_benign):
        os.system('cls')
        print(f'Benign :{i}')
        path = decompile(file)
        if path != 'err':
            temp =  extract_apis_names(path = path)
            for i in temp:
                if i in data_benign:
                    data_benign[i] += 1
                else:
                    data_benign[i] = 1
    
    for i, file in enumerate(list_adware):
        os.system('cls')
        print(f'Adware :{i}')
        path = decompile(file)
        if path != 'err':
            temp =  extract_apis_names(path = path)
            for i in temp:
                if i in data_malware:
                    data_malware[i] += 1
                else:
                    data_malware[i] = 1

    for i, file in enumerate(list_botnet):
        os.system('cls')
        print(f'Botnet :{i}')
        path = decompile(file)
        if path != 'err':
            temp =  extract_apis_names(path = path)
            for i in temp:
                if i in data_malware:
                    data_malware[i] += 1
                else:
                    data_malware[i] = 1

    for i, file in enumerate(list_ransomware):
        os.system('cls')
        print(f'Ransomeware :{i}')
        path = decompile(file)
        if path != 'err':
            temp =  extract_apis_names(path = path)
            for i in temp:
                if i in data_malware:
                    data_malware[i] += 1
                else:
                    data_malware[i] = 1

    for i, file in enumerate(list_scareware):
        os.system('cls')
        print(f'Scareware :{i}')
        path = decompile(file)
        if path != 'err':
            temp =  extract_apis_names(path = path)
            for i in temp:
                if i in data_malware:
                    data_malware[i] += 1
                else:
                    data_malware[i] = 1

    for i, file in enumerate(list_smsmalware):
        os.system('cls')
        print(f'Smsmalware :{i}')
        path = decompile(file)
        if path != 'err':
            temp =  extract_apis_names(path = path)
            for i in temp:
                if i in data_malware:
                    data_malware[i] += 1
                else:
                    data_malware[i] = 1
    
    #a = set(data_malware) - set(data_benign)

    data1 = OrderedDict(sorted(data_benign.items(), key=lambda x: x[1], reverse=True))
    data2 = OrderedDict(sorted(data_malware.items(), key=lambda x: x[1], reverse=True))

    try:
        textfile = open("api_dataset_benign.json", "w")
        json.dump(obj = data1, fp = textfile, indent=4)
        textfile = open("api_dataset_malware.json", "w")
        json.dump(obj = data2, fp = textfile, indent=4)
    except:
        pass
    finally:
        textfile.close()

    return None


if __name__ == "__main__":
    get_list_malicious_apis("C:\\Users\\marsh_000.LOrdinatueur\\Downloads\\container\\full_600")

# data1 = extract_apis_names("C:\\Users\\marsh_000.LOrdinatueur\\Desktop\\Code\\a")
# data1 = dict(Counter(data1))
# data1 = OrderedDict(sorted(data1.items(), key=lambda x: x[1], reverse=True))
# textfile = open("api_dataset.json", "w")
# json.dump(obj = data1, fp = textfile, indent=4)
# textfile.close()

