import pandas as pd
import datetime
import requests

# url = f"http://127.0.0.1:8000/scripts/XML_daily.asp" + "?date_req1=01/01/2003&date_req2=01/06/2023"
url = f"https://www.cbr.ru/scripts/XML_daily.asp" + "?date_req1=01/01/2003&date_req2=01/06/2023"

res = requests.get(url)

print(res)
