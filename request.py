import requests

url = "http://192.168.1.7:8000/execute"
data = {"code": "print(a)"}

response = requests.post(url, json=data)

# print("status code:", response.status_code)
# print("raw response:", response.text)

result = response.json()

print(result.get("output"))