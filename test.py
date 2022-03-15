import requests
import json

base_host = 'http://127.0.0.1:2000/'
header = {'content-type':'application/json'}
response = requests.get(base_host + 'api/vocab')
print(response.json())

#------------------- From the description-----------------#
words = {
    'vocab':[
        'ambassador'
    ]
}
response = requests.post(base_host + 'api/vocab', json.dumps(words), headers=header)
print(response.json())

#sponsored case
post_txt = {
"post_text": "#ad Love these cool toys at #ToysRUs. Go check them out"
}

response = requests.post(base_host + 'api/prediction', json.dumps(post_txt), headers=header)
print(response.json())

#non-sponsored case
post_txt = {
"post_text": "My new year resolution is to stay fit and healthy"
}

response = requests.post(base_host + 'api/prediction', json.dumps(post_txt), headers=header)
print(response.json())

#just add another words
add = {'vocab':['ambassador', 'Youtuber', 'blogger', 'instagrammer']}
response = requests.post(base_host + 'api/vocab', json.dumps(add), headers=header)
print(response.json())

response = requests.get(base_host + 'api/vocab')
print(response.json())

#just trying to empty txt.
empty = {'post_text':'a'}
response = requests.post(base_host + 'api/prediction', json.dumps(empty), headers=header)
print(response.json()) # output should be non-sponsored

