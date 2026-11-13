import requests


url = 'https://divar.ir/s/iran'


response = requests.get(url)

print(response)
print(response.url)
print(response.status_code)
print(response.request.headers)
print(response.request)
print(response.reason)