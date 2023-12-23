import pandas as pd


vacancies = pd.read_csv('vacancies_small.csv')

column = input().lower()
key = input().lower()
sort_by = input().lower()

vacancies.insert(loc=0, column='index', value=[i for i in range(len(vacancies))])
vacancies = vacancies.sort_values([sort_by, 'index'], ascending=[False, True])
vacancies = vacancies.fillna('')
vacancies = vacancies[vacancies[column].str.contains(key, case=False)]
print(vacancies.name.values.tolist())
