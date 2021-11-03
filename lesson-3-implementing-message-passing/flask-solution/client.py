import requests

r = requests.get('http://localhost:5000/api/orders/computers')

if r.status_code == 200:
    print(r.json())