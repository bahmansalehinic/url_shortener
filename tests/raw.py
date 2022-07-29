import requests

# res = requests.post('http://127.0.0.1:4000/url', json = {'long_url': 'www.tier.app/sdsdfsdf/34345345'})
# print(res.json())
# print(res.status_code)

res = requests.get(url='http://127.0.0.1:4000/url/https://www.tier.app/3sqbvl')
print(res.status_code)
print(res.json())