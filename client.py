import requests
from json import dumps
endpoint = "http://127.0.0.1:8000/student/create"

json_data = {"name":"max", "prn":11, "city": "hiroshima"}
data = {"name":"max", "prn":11, "city": "hiroshima"}
data = dumps(data)
# respone_data = requests.post(endpoint, json=json_data) # Can use this
respone_data = requests.post(endpoint, data=data)  # Can use this 
print(respone_data.json())