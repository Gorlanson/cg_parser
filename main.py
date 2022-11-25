import json
import requests

for page in range(1,133):
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=' + str(page)
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)

    with open('response.json', 'ab') as outf:
        outf.write(response.content)

with open('response.json') as json_file:
    data = json.load(json_file)
for symbol in data:
    print(symbol['symbol'])
