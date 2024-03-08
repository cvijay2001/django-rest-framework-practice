import requests
url = 'http://127.0.0.1:8000/studentinfo/1'


r = requests.get(url=url)

print('r',r)
data = r.json()
print('data',data)