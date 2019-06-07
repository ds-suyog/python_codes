import elasticsearch
from elasticsearch import helpers, Elasticsearch
import csv
import pandas as pd 
import git, sys; sys.path.append("{}/data".format(git.Repo('.', search_parent_directories=True).working_tree_dir))
import time

es = Elasticsearch()

file = r'data/bank_details.xls'
df = pd.read_excel(file)
df.to_csv("tmp/bank_details.csv", sep='\t', encoding='utf-8', index = False)

time1 = time.time()
reader = open('tmp/bank_details.csv', 'r') 
count = 0
dict_list = list()
dict_list_bulk = list()

for line in reader.readlines():
    line = line.strip()
    if count == 0:
        keys = line.split('\t')
    else:
        values = line.split('\t')
        dictt = zip(keys, values)
        dictt = dict(dictt)
        dict_list.append(dictt)
        temp = dict({'_index': 'indian_banks_bulk','_type': 'detail','_id': count})
        temp.update(dictt)
        dict_list_bulk.append(temp)
    count += 1

time2 = time.time()
print("data process time = ", time2 - time1)

for d in dict_list:
    es.index(index='indian_banks', doc_type='detail', body= d)
time3 = time.time()
print("one by one insertion time taken for 34716 recrods = ", time3 - time2)

helpers.bulk(es, dict_list_bulk, chunk_size=1000, request_timeout=200)
time4 = time.time()
print("bulk insertion time taken for 34716 records = ", time4 - time3)
