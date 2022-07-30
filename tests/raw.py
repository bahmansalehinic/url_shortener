import requests

res = requests.put('http://127.0.0.1:4000/url', json = {'url': 'www.tier.app', 'new_url':'https://www.tier.app/en/sustainability'})
print(res.json())
print(res.status_code)

# res = requests.get(url='http://127.0.0.1:4000/cMJDU')
#
# print(res.status_code)
# print(res.json())