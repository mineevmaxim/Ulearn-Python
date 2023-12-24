import pandas as pd
from collections import Counter


vacancies = pd.read_csv('vacancies_small.csv')
result = Counter()
name = input().lower()

vacancies = vacancies[vacancies['name'].str.contains(name, case=False)].dropna(subset=['key_skills'])
skills = [x.replace('\r', '').split('\n') for x in vacancies.key_skills.values.tolist()]

result_skills = []
for x in skills:
    result_skills.extend(x if isinstance(x, list) else [x])

result.update(result_skills)

print(result.most_common(5))
