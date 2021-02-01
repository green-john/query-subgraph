import requests
import pprint

import sys

query = ""
with open(sys.argv[1], "r") as f:
    query = f.read()

url = "https://api.thegraph.com/subgraphs/name/1inch-exchange/one-inch-v2"
response = requests.post(url, json={
    "query": query
})

print(response.status_code)
pprint.pprint(response.json())
