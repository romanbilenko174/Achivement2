import requests

url = "http://127.0.0.1:5000"
number = 43
payload = {"number": number}
response = requests.post(url, json=payload)
print(response.json())
