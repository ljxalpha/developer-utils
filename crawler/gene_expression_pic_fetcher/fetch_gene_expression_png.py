import requests
import json
from lxml import html,etree
import pandas as pd
import numpy as np

geneList = ["IL22","A1BG","A2M"]
for gene in geneList:
    url = "https://cdn.genecards.org/rna-expression-v4-12/gene_expression_{0}.png".format(gene)
    response = requests.get(url)
    png = open("/home/kate/LJX/developer-utils/crawler/gene_expression_pic_fetcher/img/{0}.png".format(gene), "wb")
    png.write(response.content)
    png.close()