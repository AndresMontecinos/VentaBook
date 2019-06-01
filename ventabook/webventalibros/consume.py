import json
import urllib
import urllib.request


response = urllib.request.urlopen("http://localhost:8000/bodegas/")
data = json.loads(response.read())
print(data)
for d in data:
    print(d)

