import csv
import re


def parse_datetime(string):
    return '.'.join(string.split('T')[0].split('-')[::-1])


def str_to_bool(string):
    if string.lower == 'true':
        return True
    return False


def format_string(string):
    if string == 'False':
        return 'Нет'
    if string == 'True':
        return 'Да'
    pattern = r'<.*?>'
    clear_string = re.sub(pattern, '', string).strip()
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


def formatter(row: dict, dic_naming: dict, experience, currency, true_false):
    result = {}
    for item in row:
        if item in ['salary_from', 'salary_to', 'salary_gross', 'salary_currency'] and dic_naming['salary'] not in result:
            result[dic_naming['salary']] = f"{int(float(row['salary_from'])):,}".replace(",", " ") + " - " + f"{int(float(row['salary_to'])):,}".replace(",", " ") + f" ({currency[row['salary_currency']]})" + f" ({'С вычетом налогов' if row['salary_gross'] == 'Нет' else 'Без вычета налогов'})"
        elif item == 'experience_id':
            result[dic_naming[item]] = experience[row[item]]
        elif row[item].lower in true_false:
            result[dic_naming[item]] = true_false[row[item].lower()]
        elif item == 'published_at':
            result[dic_naming[item]] = parse_datetime(row[item])
        elif item not in ['salary_from', 'salary_to', 'salary_gross', 'salary_currency']:
            result[dic_naming[item]] = row[item]
        else:
            continue
    return result


def print_vacancies(data_vacancies, dic_naming, experience, currency, true_false):
    for i in range(len(data_vacancies)):
        clear_dict = formatter(data_vacancies[i], dic_naming, experience, currency, true_false)
        for item in clear_dict:
            print(f'{item}: {clear_dict[item]}')
        if i != len(data_vacancies) - 1:
            print()


dic_naming = {
    'name': 'Название',
    'description': 'Описание',
    'key_skills': 'Навыки',
    'experience_id': 'Опыт работы',
    'premium': 'Премиум-вакансия',
    'employer_name': 'Компания',
    'salary': 'Оклад',
    'area_name': 'Название региона',
    'published_at': 'Дата публикации вакансии',
}

experience = {
    "noExperience": "Нет опыта",
    "between1And3": "От 1 года до 3 лет",
    "between3And6": "От 3 до 6 лет",
    "moreThan6": "Более 6 лет",
}

currency = {
    "AZN": "Манаты",
    "BYR": "Белорусские рубли",
    "EUR": "Евро",
    "GEL": "Грузинский лари",
    "KGS": "Киргизский сом",
    "KZT": "Тенге",
    "RUR": "Рубли",
    "UAH": "Гривны",
    "USD": "Доллары",
    "UZS": "Узбекский сум",
}

true_false = {
    'true': 'Да',
    'false': 'Нет'
}

file_name = input()
file_name = input()

rows, titles = csv_reader(file_name)

data_vacancies = csv_filer(rows, titles)
print_vacancies(data_vacancies, dic_naming, experience, currency, true_false)