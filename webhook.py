import requests
import json

yourKey = '193119f42d583601d5095b462bde9300'
yourToken = '051f6534202857a75e06a3c58358840f62a4e54fe268648aad672465cb2cb4c6'

url = f"https://api.trello.com/1/webhooks?key={yourKey}&token={yourToken}"

query = {
   'callbackURL': 'http://127.0.0.1:5000/webhook',
   'idModel': '5ebab65d387cbc84d05ff9cc'
}

response = requests.request(
   "POST",
   url,
   params=query
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))