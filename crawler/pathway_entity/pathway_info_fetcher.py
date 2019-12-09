import requests
from lxml import html 
import pandas as pd
import numpy as np
pmoidFile = file("/home/kate/LJX/bmap-20180710-down/crawler/pmoid.list", "r")
pmoidList = pmoidFile.readlines()
pmoidFile.close()


# columnSet = set()
# columnSet.add("PMOID")
# columnSet.add("pathway_name")
# pathwayList = []
# baseURL = "http://docker.scbit.org/pmapp/detail/Pathway/"
# count = 1
# for pmoid in pmoidList: 
#     pathwayEntity = {}
#     url = baseURL + pmoid
#     url = url.replace("\n", "")
#     print "Fetching NO." + str(count) + " pathway : " + url
#     count = count + 1
#     dom = html.fromstring(requests.get(url).content)
#     res = dom.xpath("""/html/body/div[3]/div/div/div/div/div/div[1]/div[2]""")
#     dlList = dom.xpath("""/html/body/div[3]/div/div/div/div/div/div[1]/div[2]/dl""")
#     if(len(dlList) == 0):
#         print "ERROR " + pmoid
#         continue
#     for dl in dlList:
#         column = dl.xpath("dt/text()")[0]
#         value = ""
#         aList = dl.xpath("dd/a")
#         for a in aList:
#             value = value+ a.xpath("text()")[0] + " " 
#         value = value[:-1]
#         if (not column in columnSet):
#             columnSet.add(column)
#         pathwayEntity[column] = value
#     pathwayEntity["PMOID"] = "PMO:" + pmoid.replace("\n", "")
#     pathwayEntity["pathway_name"] = dom.xpath("/html/body/div[3]/div/div/div/div/div/div[1]/div[1]/div/a/text()")[0]
#     pathwayList.append(pathwayEntity)

# columnList = list(columnSet)

# np.save("/home/kate/LJX/bmap-20180710-down/crawler/column_list", columnList)
# np.save("/home/kate/LJX/bmap-20180710-down/crawler/pathway_list", pathwayList)

# columnList = list(np.load("/home/kate/LJX/bmap-20180710-down/crawler/column_list.npy"))
# pathwayList = np.load("/home/kate/LJX/bmap-20180710-down/crawler/pathway_list.npy")
# pathwayList = list(pathwayList)

columnList.remove("Cell Type")
columnList.append("cell_type")
columnList.append("PMOID")
columnList.append("pathway_name")

count = 1

sqlFile = open("/home/kate/LJX/bmap-20180710-down/crawler/pathway.sql", "a")
sqlFile.write("\n" * 4)
sqlHead= """insert into pathway_entity ("""
for col in columnList:
    sqlHead  = sqlHead + col + ","
sqlHead = sqlHead[:-1]
sqlHead = sqlHead + """) values ("""
sqlTail = ");"
for pathway in pathwayList:
    print "Generating SQL for NO." + str(count) + " pathway."
    count = count + 1
    sqlBody = """"""
    for col in columnList:
        value = None
        try:
            string = pathway[col]
            string.replace(";", "; ")
            string = string.replace("\"", "'")
            value = """\"""" + string + """\"""" 
        except Exception:
            value = "NULL"
        sqlBody = sqlBody + value + ","
    sqlBody = sqlBody[:-1]
    sql = sqlHead + sqlBody + sqlTail + "\n"
    print sql
    sqlFile.write(sql)
print "\n\nAll finished!!!\n\n"
sqlFile.close()



