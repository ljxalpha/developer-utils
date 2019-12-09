import requests
import json
from lxml import html 
import pandas as pd
import numpy as np

pathwayFile = file("/home/kate/LJX/developer-utils/crawler/pathway_view/pathway_name.list", "r")
pathwayList = pathwayFile.readlines()
pathwayFile.close()

url = "http://localhost:8001/searchnet"
count = 1
errorList = []
# recordFile = file("/home/kate/LJX/developer-utils/crawler/pathway_view/record.txt", "a")
timeCostList = []
for path in pathwayList: 

    print "Caching NO." + str(count) + " pathway : " + path
    data = {"searchType": "pathway","keyword": path,"keywordType": "symbol"}
    postRequest = requests.post(url, data = data)
    timeCost = postRequest.elapsed.microseconds / (float)(1000000)
    res = json.loads(postRequest.content)
    timeCostList.append(timeCost)
    # record = str(count) + ";" + path.replace("\n","") + ";" + str(timeCost) + "\n"
    # recordFile.write(record)
    count = count + 1
    if(res["message"] != "successfully"):
        errorList.append(path)
print timeCostList
print errorList
# recordFile.close()