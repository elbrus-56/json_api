import logging

import requests
from jsonrpcclient import request, parse, Ok

response = requests.post("http://localhost:5000/", json=request("mull", params=(4, 2)))
# response = requests.post("http://localhost:5000/", json=request("ping"))

parsed = parse(response.json())
if isinstance(parsed, Ok):
    print(parsed.result)
else:
    logging.error(parsed.message)
