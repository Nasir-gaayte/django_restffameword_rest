import requests

# endpoint = "http://httpbin.org/anything"
endpoint = "http://localhost:8008/api/" #http://127.0.0.1:8008/api/


get_response =  requests.get(endpoint)
print(get_response.text)
print(get_response.status_code)

print(get_response.json())
