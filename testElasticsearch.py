from elasticsearch import Elasticsearch
#from elasticsearch_dsl import Search, Q
import requests
import json
import yaml

from yahoo_finance import Share
from pprint import pprint

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# #delete index if exists
# if es.indices.exists('stockprice'):
#     es.indices.delete(index='stockprice')
#     
# #mapping
# stockmapping = '''{"mappings":{"stock":{"properties":{"High":{"type":"double"},"Low":{"type":"double"},"Open":{"type":"double"},"Close":{"type":"double"},"Adj_Close":{"type":"double"},"Volume":{"type":"long"},"Date":{"type":"date"},"Symbol":{"type":"string"}}}}}'''
# es.indices.create(index='stockprice', ignore=400, body=stockmapping)

symbol = 'BAC'
stock = Share(symbol)
stock.refresh()
price = stock.get_historical('2016-04-01', '2016-04-25')
i = 1
for x in price:
    print json.dumps(x, indent=4)
    es.index(index='stockprice', doc_type='stock', id=i, body=x, ignore=400)
    i=i+1
 
# es.indices.put_mapping(index='stockprice', doc_type='stock', body=stockmapping)

#let's iterate over swapi people documents and index them
# r = requests.get('http://localhost:9200') 
# i = 1
# while r.status_code == 200:
#     r = requests.get('http://swapi.co/api/people/'+ str(i))
#     es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
#     i=i+1
 
# es.get(index='sw', doc_type='people', id=5)
# es.search(index="sw", body={"query": {"match": {'name':'Darth Vader'}}})
# es.search(index="sw", body={"query": {"prefix" : { "name" : "lu" }}})
# searchresult = es.search(index="sw", q="Luke")['hits']['hits'][0]
# print searchresult
# 
# #parsed = yaml.safe_load(searchresult)
# 
# print json.dumps(searchresult, indent=4)