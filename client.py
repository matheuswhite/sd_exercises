import requests

url = 'http://127.0.0.1:5000/university'
#url = 'http://[::1]:5000/university'

req = requests.get(url)
print req.status_code
print req.text

req = requests.post(url, data={'name': 'Universidad de Chile'})
print req.status_code
print req.text

req = requests.put(url, data={'index': 6, 'name': 'Universidade Federal Fluminense'})
print req.status_code
print req.text

req = requests.delete(url + '/5')
print req.status_code
print req.text

req = requests.delete(url + '/25')
print req.status_code
print req.text
