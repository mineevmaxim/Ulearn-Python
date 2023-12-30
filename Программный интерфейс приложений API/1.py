import requests
import json


city = input()
BASE_URL = "http://127.0.0.1:8000"
i = 0
while True:
    i += 1
    res = requests.get('http://127.0.0.1:8000/vacancies/' + str(i))
    if "error" in res.text:
        break

    json_res = json.loads(res.text)

    if str(json_res.get('area_name')).strip() == city:
        print(json_res)
        