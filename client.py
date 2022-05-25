import requests
from json import dumps
endpoint = "http://127.0.0.1:8000/student/create"

json_data = {"name":"max", "prn":11, "city": "hiroshima"}
data = {"name":"max", "prn":11, "city": "hiroshima"}


respone_data = requests.post(endpoint, json=dumps(json_data), data=data)
print(respone_data)