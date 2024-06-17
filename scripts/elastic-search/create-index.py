from elasticsearch import Elasticsearch
import yaml

config = yaml.load(open('./config/ElasticSearch.yml', 'r'), Loader=yaml.Loader)

ES_HOST = config['host']
ES_PORT = config['port']
USERNAME = config['username']
PASSWORD = config['password']

es = Elasticsearch(  
    [{'host': ES_HOST, 'port': ES_PORT, 'scheme': 'http'}],
    basic_auth=(str(USERNAME), str(PASSWORD))
)  

if es.ping():  
    print('Yes, I can connect to Elasticsearch!')  
else:  
    print('No, I cannot connect to Elasticsearch!')

index_name = "mdata-background-management"

mappings = {
    "properties": {  
        "id": {  
            "type": "long"  
        },  
        "name": {  
            "type": "text",  
            "fields": {  
                "keyword": {  
                    "type": "keyword",  
                    "ignore_above": 256
                }  
            }  
        },  
        "status": {  
            "type": "integer"  
        },  
        "createTS": {  
            "type": "long"  
        },  
        "modifyTS": {  
            "type": "long"  
        }  
    }
}

es.index()

if not es.indices.exists(index=index_name):
    res = es.indices.create(
        index=index_name,
        body={
            'mappings': mappings
        }
    )
    print(f'create {index_name}, result: {res}')
else:
    print(f'{index_name} already exists!')
  
# # 创建索引  
# es.indices.create(index='my_index', settings=settings, body=mappings)