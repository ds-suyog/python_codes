import elasticsearch
from elasticsearch import helpers, Elasticsearch
import csv
import pandas as pd 

es = elasticsearch.Elasticsearch()

file = r'/home/suyog/data/bank_details.xls'
df = pd.read_excel(file)
df.to_csv("output.csv", sep='\t', encoding='utf-8', index = False)

reader = open('/home/suyog/github/IndianBanks/output.csv', 'r') 
count = 0
keys =  []
values = []
for line in reader.readlines():
  if count == 0:
    keys = line.split('\t')
    count += 1
  else:
    values = line.split('\t')
    dictt = zip(keys, values)
    dictt = dict(dictt)
    es.index(index='indian_bank', doc_type='bank_test', body= dictt)
    #helpers.bulk(es, dict(dictt), index='my-index2', doc_type='my-type2')


