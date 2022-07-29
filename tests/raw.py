import requests

res = requests.post('http://127.0.0.1:4000/url', json = {'long_url': 'wwww.gooooo'})
print(res.json())
print(res.status_code)