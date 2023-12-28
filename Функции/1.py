import csv
import re


def format_string(string):
    if string == 'False':
        return 'Нет'
    if string == 'True':
        return 'Да'
    pattern = r'<.*?>'
    clear_string = re.sub(pattern, '', string).strip()
    if '\n' in clear_string:
        clear_string = clear_string.replace('\n', ', ')
    clear_string = ' '.join(clear_string.split())
    return clear_string


def csv_reader(file_name):
    with open(file_name, encoding='utf-8-sig') as file:
        file_reader = list(csv.reader(file, delimiter=','))
        titles = file_reader[0]
        rows = []
        for row in file_reader[1:]:
            if '' not in row and len(row) == len(titles):
                rows.append(row)
    return rows, titles


def csv_filer(reader, list_naming):
    dicts = []
    for row in reader:
        data = {}
        for i in range(len(list_naming)):
            data[list_naming[i]] = format_string(row[i])
        dicts.append(data)
    return dicts


def print_vacancies(data_vacancies, dic_naming):
    for i in range(len(data_vacancies)):
        for item in data_vacancies[i]:
            print(f'{dic_naming[item]}: {data_vacancies[i][item]}')
        if i != len(data_vacancies) - 1:
            print()


dic_naming = {
    'name': 'Название',
    'description': 'Описание',
    'key_skills': 'Навыки',
    'experience_id': 'Опыт работы',
    'premium': 'Премиум-вакансия',
    'employer_name': 'Компания',
    'salary_from': 'Нижняя граница вилки оклада',
    'salary_to': 'Верхняя граница вилки оклада',
    'salary_gross': 'Оклад указан до вычета налогов',
    'salary_currency': 'Идентификатор валюты оклада',
    'area_name': 'Название региона',
    'published_at': 'Дата и время публикации вакансии',
}

file_name = input()
rows, titles = csv_reader(file_name)

data_vacancies = csv_filer(rows, titles)
print_vacancies(data_vacancies, dic_naming)