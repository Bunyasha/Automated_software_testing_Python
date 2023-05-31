import requests
import yaml

with open('logpass.yaml') as f:
    data = yaml.safe_load(f)

name = data['user']
passwd = data['passwd']
title = data['title']
description = data['description']
content = data['content']


def new_post(token):
    returns = requests.post('https://test-stand.gb.ru/gateway/posts', headers={'X-Auth-Token': token},
                             data={'title': title, 'description': description, 'content': content})
    return returns.json()['item']

def get(token):
    g = requests.get('https://test-stand.gb.ru/api/posts', headers={'X-Auth-Token': token})
    listd = [i['description'] for i in g.json()['data']]
    return listd


def test_hw1(login, newpost_text):
    assert newpost_text in get(login)