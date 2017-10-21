import requests
url = "http://localhost:8000/entries/"
headers = {'Authorization': 'Token 848804ca8cb4f7287f57a02ea0cdbb2c0628da6d'}
r = requests.get(url, headers=headers)
print(r.text)
