import urllib.request

with urllib.request.urlopen('http://www.python.org/') as f:
    print(f.read(300).decode('utf-8'))  # ograniczamy się do 300 B

#-------------

# pip install requests -- albo requirements.txt
import requests

r = requests.get('http://www.python.org/')
r.raise_for_status()
print(r.status_code, r.text[:300])

r = requests.get("https://wttr.in/?format=j1")
r.raise_for_status()
j = r.json()
print(j['nearest_area'][0]['areaName'][0]['value'])
print(int(j['current_condition'][0]['temp_C']))

#r = requests.post("https://example.com", data='{"test": ["Example", "data"]}')
r = requests.post("https://example.com", json={"test": ["Example", "data"]}, headers={'Accept': 'application/json'})
print(r.request.headers)
print(r.status_code, r.text[:300])

#authentication: JWT

# a co z serwerem?
#  python -m http.server --- udostępnianie plików na szybko (niebezpieczne)
#  flask --- strony internetwe i aplikacje REST
#  django --- strony internetowe

#------ json i yaml

import json
s = '{"prosty": "przyklad"}'
d = json.loads(s)  # ładowanie ze stringa
print(d['prosty'])
d['prosty'] = True
s2 = json.dumps(d)
print(s2)

with open("example.json", encoding='utf-8') as f:
    d = json.load(f)
print(d)

with open("example_output.json", 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=4)

# pip install PyYAML
import yaml

print(yaml.safe_dump(d))
with open("example.yaml") as f:
    s = f.read()
print(yaml.safe_load(s))

with open("example.yaml") as f:
    print(yaml.safe_load(f))