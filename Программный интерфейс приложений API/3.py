import pandas as pd
import requests
from io import StringIO
import lxml


currency_array = ["BYR", "USD", "EUR", "KZT", "UAH", "AZN", "KGS", "UZS", "GEL"]
data = []
date = pd.to_datetime('2003-01-01')
end_date = pd.to_datetime('2023-07-01')

while date < end_date:
    date_str = date.strftime('%d/%m/%Y')
    # url = f"http://127.0.0.1:8000/scripts/XML_daily.asp?date_req={date_str}"
    url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={date_str}"
    res = requests.get(url)
    df = pd.read_xml(StringIO(res.text))
    df = df[['CharCode', 'Value', 'Nominal']]
    df['Value'] = df['Value'].str.replace(',', '.').astype(float)
    # df['Nominal'] = df['Nominal'].astype(float)
    # df['Value_per_unit'] = round(df['Value'] / df['Nominal'], 10)
    df = df[df['CharCode'].isin(currency_array)].set_index('CharCode').T
    df.insert(0, 'date', pd.to_datetime(date_str, format='%d/%m/%Y').strftime('%Y-%m'))
    data.append(df.to_dict(orient='records')[0])
    date = (date + pd.DateOffset(days=32)).replace(day=1)

df = pd.DataFrame(data)
df.to_csv("student_works/currency.csv", index=False)
