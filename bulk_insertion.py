import elasticsearch
from elasticsearch import helpers, Elasticsearch
import csv
import pandas as pd 
import git, sys; sys.path.append("{}/data".format(git.Repo('.', search_parent_directories=True).working_tree_dir))

es = Elasticsearch()

file = r'data/bank_details.xls'
df = pd.read_excel(file)
df.to_csv("tmp/bank_details.csv", sep='\t', encoding='utf-8', index = False)

reader = open('tmp/bank_details.csv', 'r') 
count = 0
keys =  []
values = []
dict_list = list()
for line in reader.readlines():
    line = line.strip()
    if count == 0:
        keys = line.split('\t')
    else:
        values = line.split('\t')
        dictt = zip(keys, values)
        dictt = dict(dictt)
        dictt_bulk = dict()
        dictt_bulk.update({'_index': 'indian_banks_bulk','_type': 'detail','_id': count})
        dict_list.append(dictt_bulk)
        es.index(index='indian_banks', doc_type='detail', body= dictt)
    count += 1
    if count == 5:
        break

helpers.bulk(es, dict_list, chunk_size=1000, request_timeout=200)
