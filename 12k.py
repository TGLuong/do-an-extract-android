import json
from Lib.AndroidDetection import AndroidDetection
from Lib.library import *
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score

def split_train():
    adware_path = './Extract/new_train_11k/adware.json'
    banking_path = './Extract/new_train_11k/banking.json'
    benign_path = './Extract/new_train_11k/benign.json'
    riskware_path = './Extract/new_train_11k/riskware.json'
    smsmalware_path = './Extract/new_train_11k/smsmalware.json'

    adware = open(adware_path, 'r')
    adware = json.load(adware)

    banking = open(banking_path, 'r')
    banking = json.load(banking)

    benign = open(benign_path, 'r')
    benign = json.load(benign)

    riskware = open(riskware_path, 'r')
    riskware = json.load(riskware)

    smsmalware = open(smsmalware_path, 'r')
    smsmalware = json.load(smsmalware)

    adware_train = adware[100:]
    adware_test = adware[:100]

    print("adware train: " + str(len(adware_train)))
    print("adware test: " + str(len(adware_test)))


    banking_train = banking[100:]
    banking_test = banking[:100]

    print("banking train: " + str(len(banking_train)))
    print("banking test: " + str(len(banking_test)))

    benign_train = benign[100:]
    benign_test = benign[:100]

    print("benign train: " + str(len(benign_train)))
    print("benign test: " + str(len(benign_test)))

    riskware_train = riskware[100:]
    riskware_test = riskware[:100]

    print("riskware train: " + str(len(riskware_train)))
    print("riskware test: " + str(len(riskware_test)))

    smsmalware_train = smsmalware[100:]
    smsmalware_test = smsmalware[:100]

    print("sms train: " + str(len(smsmalware_train)))
    print("sms test: " + str(len(smsmalware_test)))

    train_11k = []
    test_11k = []

    for e in adware_train:
        train_11k.append(e)
    
    for e in banking_train:
        train_11k.append(e)

    for e in benign_train:
        train_11k.append(e)

    for e in riskware_train:
        train_11k.append(e)
    
    for e in smsmalware_train:
        train_11k.append(e)
    
    print(len(train_11k))

    
    for e in adware_test:
        test_11k.append(e)
    
    for e in banking_test:
        test_11k.append(e)
    
    for e in benign_test:
        test_11k.append(e)
    
    for e in riskware_test:
        test_11k.append(e)
    
    for e in smsmalware_test:
        test_11k.append(e)
    
    print(len(test_11k))

    train_file = open("Extract/new_train_11k/training_11k.json", 'w')
    train_file.write(json.dumps(train_11k, indent=4))

    test_file = open("Extract/new_train_11k/testting_11k.json", "w")
    test_file.write(json.dumps(test_11k, indent=4))

    
    return



def testing():
    # test = open("Extract/new_train_11k/testting_11k.json", 'r')
    # test = json.load(test)
    # label_test = label(test)
    test_vector = load_pkl("test_vector.pkl")
    label_test = load_pkl("test_label.pkl")

    # mal_ben_label = []

    # for e in label_test:
    #     if e == "benign":
    #         mal_ben_label.append("benign")
    #     else:
    #         mal_ben_label.append("malware")

    model = AndroidDetection()
    predict = []
    for i,e in enumerate(test_vector):
        print(i)
        result = model.predict_feature_vector(e)
        predict.append(result)
    
    # save_pkl("test_vector.pkl", vectors)

    print("accuracy score = {:.4f}".format(accuracy_score(label_test, predict)))
    print("f1 score = {:.4f}".format(f1_score(label_test, predict, average="macro")))
    print("recall score = {:.4f}".format(recall_score(label_test, predict, average="macro")))
    print("precision score = {:.4f}".format(precision_score(label_test, predict, average="macro")))


def abc():
    test = open("Extract/new_train_11k/testting_11k.json", 'r')
    test = json.load(test)

    for e in test:
        if e['label'] == "riskware":
            print(e['name'])
    return

if __name__ == "__main__" :
    abc()


    
