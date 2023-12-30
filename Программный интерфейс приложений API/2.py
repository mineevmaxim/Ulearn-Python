import requests


BASE_URL = "http://127.0.0.1:8000"

new_product = {
    "name": input(),
    "salary": input(),
    "area_name": input(),
}

response = requests.post(f"{BASE_URL}/vacancies", json=new_product)
