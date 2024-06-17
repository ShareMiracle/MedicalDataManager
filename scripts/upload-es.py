import requests as r
import json

server = 'http://localhost:8080'

def update_data(data_json: dict):
    payload = json.dumps(data_json)
    headers = {
        'Content-Type': 'application/json'
    }
    res = r.put(server + '/es/addItem', data=payload, headers=headers)
    if res.status_code == 200:
        print(res.json())

if __name__ == '__main__':
    storage = json.load(open('./data/storage.json', 'r'))
    for item in storage['storage']:
        update_data(item)