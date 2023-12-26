import pandas as pd
import numpy as np

vacancies = pd.read_csv('vacancies_small.csv')
vacancies = (vacancies[vacancies.salary_currency == 'RUR'])[['area_name', 'salary_from', 'salary_to']].fillna(-1)

vacancies['salary_from'] = np.where(vacancies['salary_from'] == -1, vacancies['salary_to'], vacancies['salary_from'])
vacancies['salary_to'] = np.where(vacancies['salary_to'] == -1, vacancies['salary_from'], vacancies['salary_to'])

vacancies.insert(loc=len(vacancies.columns), column='salary', value=(vacancies['salary_from'] + vacancies['salary_to']) / 2)

del vacancies['salary_from']
del vacancies['salary_to']

vacancies_counts = vacancies.area_name.value_counts().to_dict()

areas = {}

for vacancy in vacancies.to_dict('index').values():
    if (area_name := vacancy['area_name']) not in areas:
        areas[area_name] = vacancy['salary']
    else:
        areas[area_name] += vacancy['salary']

areas = {key: value / vacancies_counts[key] for (key, value) in areas.items()}
areas = {key: value for (key, value) in sorted(areas.items(), key=lambda x: (-x[1], x[0]))}

print(areas)