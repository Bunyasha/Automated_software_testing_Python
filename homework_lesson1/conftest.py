import pytest 
import requests
import yaml

with open('logpass.yaml') as f:
    data = yaml.safe_load(f)

name = data['user']
passwd = data['passwd']
title = data['title']
description = data['description']
content = data['content']



@pytest.fixture()
def login():
    r = requests.post('https://test-stand.gb.ru/gateway/login', data={'username': name, 'password': passwd})
    return r.json()['token']


#@pytest.fixture()
#def new_post(token):
 #   returns = requests.post('https://test-stand.gb.ru/gateway/posts', headers={'X-Auth-Token': token},
  #                           data={'title': title, 'description': description, 'content': content})
   # return returns.json()['item']

@pytest.fixture()
def newpost_text():
    return 'description of new post'

