import json
import requests

result=json.dumps({"1": {"value": 6948, "weight": 10316, "volume": 12, "items": [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1]}, "2": {"value": 4367, "weight": 10220, "volume": 12, "items": [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0]}})
print(result)
url ='https://cit-home1.herokuapp.com/api/ga_homework'
js = {'content-type': 'application/json'}
r = requests.post(url, data=result,headers=js)
print(r.json())
