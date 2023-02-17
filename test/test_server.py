import sys

import pytest
import requests

sys.path.append("/home/ubuntu/PycharmProjects/json-api/")


# Test main page
def test_do_get_code_200():
    url = 'http://127.0.0.1:5000/'
    response = requests.get(url)
    assert response.status_code == 200


def test_do_get_text():
    url = 'http://127.0.0.1:5000/'
    response = requests.get(url)
    assert response.text == '<a href="http://127.0.0.1:5000/api/v1/">Link to json file</a>'


# Test page api
@pytest.fixture()
def send_request(request):
    url = 'http://127.0.0.1:5000/api/v1/'
    return requests.post(url, json=request.param)


@pytest.mark.parametrize("send_request", [
    {"jsonrpc": "2.0", "method": "divide", "params": [1, 1], "id": 8}
], indirect=["send_request"])
def test_do_get_with_some_requests(send_request):
    request = send_request
    url = 'http://127.0.0.1:5000/api/v1/'
    response = requests.get(url)
    assert response.status_code == 200
    response = requests.get(url)
    assert response.status_code == 404
    response = requests.get(url)
    assert response.status_code == 404


@pytest.mark.parametrize("send_request", [
    {"jsonrpc": "2.0", "method": "divide", "params": [1, 1]},
    {"jsonrpc": "2.0"},
    "567788",
    90000000000,
    {}
], indirect=["send_request"])
def test_do_get_with_wrong_request(send_request):
    request = send_request
    url = 'http://127.0.0.1:5000/api/v1/'
    response = requests.get(url)
    assert response.status_code == 404


@pytest.mark.parametrize("send_request, expected", [
    ({}, 200),
    ({"jsonrpc": "2.0", "method": "divide", "params": [2, 8], "id": 8}, 200),
    ({"jsonrpc": "2.0"}, 200)
], indirect=["send_request"])
def test_do_post_code_200_with_params(send_request, expected):
    response = send_request
    assert response.status_code == expected


@pytest.mark.parametrize("send_request, expected", [
    ({"jsonrpc": "2.0", "method": "divide", "params": [1, 1], "id": 8},
     {"jsonrpc": "2.0", "result": 1.0, "id": 8}),
    ({"jsonrpc": "2.0", "method": "add", "params": [1, 0], "id": 8},
     {"jsonrpc": "2.0", "result": 1, "id": 8}),
    ({"jsonrpc": "2.0", "method": "sub", "params": [5, 1], "id": 8},
     {"jsonrpc": "2.0", "result": 4, "id": 8}),
    ({"jsonrpc": "2.0", "method": "mull", "params": [3, 2], "id": 9},
     {"jsonrpc": "2.0", "result": 6, "id": 9})
], indirect=["send_request"])
def test_do_post_with_params(send_request, expected):
    request = send_request
    assert request.json() == expected


@pytest.mark.parametrize("send_request, expected", [
    ({"jsonrpc": "2.0", "method": "divide", "params": [1, 0], "id": 8},
     {'id': 8, 'jsonrpc': '2.0', 'result': 'Нельзя делить на ноль'}),
], indirect=["send_request"])
def test_do_post_with_null(send_request, expected):
    request = send_request
    assert request.json() == expected


@pytest.mark.parametrize("send_request", [
    ({"method": "divide", "params": [4, 2], "id": 8}),
    ({"method": "sub", "params": [4, 2], "id": 8, "jsonrpc": "2.0", 1: 123},),
    ({},),
    ([],),
    ({"method1": "sub", "params": [4, 2], "id": 8, "jsonrpc": "2.0"},),
    ({"method": "sub", "params": [4, 2], "id": 8, "jsonrpcs": "2.0"},),
    ({"method": "sub", "": [4, 2], "id": 8, "jsonrpc": "2.0"},),
    ({"method": "sub", "params": (4, 2), "id": 8, "jsonrpc": "2.0"},),
    ({"method": "sub", "params": ["4", 2], "id": 8, "jsonrpc": "2.0"},),
    ({"method": "sub", "params": [4, "2"], "id": 8, "jsonrpc": "2.0"},),
    ({"method": "sub", "params": [4, 2], "id": "8", "jsonrpc": "2.0"},),
    ({"method": "sub", "params": [4, 2], "id": 8, "jsonrpc": 2.0},),
    ({"method": ["sub"], "params": [4, 2], "id": 8, "jsonrpc": "2.0"},),
    ({"method": None, "params": [4, 2], "id": 8, "jsonrpc": "2.0"},),

], indirect=["send_request"])
def test_do_post_with_key_error(send_request):
    request = send_request
    assert request.text == "Error key"
