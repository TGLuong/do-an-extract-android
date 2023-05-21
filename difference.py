import json
from typing import OrderedDict


with open("api_dataset_benign.json") as json_file:
    benign = json.load(json_file)

with open("api_dataset_malware.json") as json_file:
    malware = json.load(json_file)


benign250 = list((dict(sorted(benign.items(), key=lambda x: x[1], reverse=True)[:400])).keys())

malware250 = list(dict(sorted(malware.items(), key=lambda x: x[1], reverse=True)[:400]).keys())

api_list = benign250 + malware250
api_list = set(api_list)
api_list = list(api_list)

try:
    textfile = open("api_dataset_new_500.json", "w")
    json.dump(obj = api_list, fp = textfile, indent=4)
except:
    pass
finally:
    textfile.close()