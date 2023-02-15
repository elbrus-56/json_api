import sys
import pytest
import requests
import json

sys.path.append("/home/ubuntu/PycharmProjects/json-api/")


def test_do_get_code_200():
    url = 'http://127.0.0.1:5000/'
    response = requests.get(url)
    assert response.status_code == 200


def test_do_get_code_text():
    url = 'http://127.0.0.1:5000/'
    response = requests.get(url)
    assert response.text == '<h1>hello !</h1>'


def test_do_post_code_200():
    url = 'http://127.0.0.1:5000/'
    response = requests.post(url)
    assert response.status_code == 200


@pytest.mark.parametrize("params, expected", [
    ({}, 200),
    ({"jsonrpc": "2.0", "method": "divide", "params": [2, 8], "id": 8}, 200),
    ({"jsonrpc": "2.0"}, 200)
])
def test_do_post_code_200_with_params(params, expected):
    url = 'http://127.0.0.1:5000/'
    response = requests.post(url, json=params)
    assert response.status_code == expected


@pytest.mark.parametrize("params, expected", [
    ({"jsonrpc": "2.0", "method": "divide", "params": [1, 1], "id": 8},
     {"jsonrpc": "2.0", "result": 1.0, "id": 8}),
    ({"jsonrpc": "2.0", "method": "add", "params": [1, 9], "id": 8},
     {"jsonrpc": "2.0", "result": 10, "id": 8}),
    ({"jsonrpc": "2.0", "method": "sub", "params": [5, 1], "id": 8},
     {"jsonrpc": "2.0", "result": 4, "id": 8}),
    ({"jsonrpc": "2.0", "method": "mull", "params": [3, 2], "id": 8},
     {"jsonrpc": "2.0", "result": 6, "id": 8})
])
def test_do_post_with_params(params, expected):
    url = 'http://127.0.0.1:5000/'
    response = requests.post(url, json=params)
    ans = json.loads(response.text)
    assert ans == expected
