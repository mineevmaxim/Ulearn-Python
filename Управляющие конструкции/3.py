import csv
import re


def format_string(string):
    pattern = r'<.*?>'
    clear_string = re.sub(pattern, '', string).strip()
    if '\n' in clear_string:
        clear_string = clear_string.replace('\n', ', ')
    clear_string = ' '.join(clear_string.split())
    return clear_string


def print_salaries(word, salaries):
    print(f'Самые {word} зарплаты:')
    for index in range(len(salaries)):
        if index == 10:
            break
        salary = salaries[index]["salary"]
        last_word = 'рублей'
        if salary % 10 == 1:
            last_word = 'рубль'
        elif salary % 10 in [2, 3, 4]:
            last_word = 'рубля'
        print(f'    {index + 1}) {salaries[index]["name"]} в компании "{salaries[index]["employer_name"]}" - {int(salary)} {last_word} (г. {salaries[index]["area_name"]})')


def print_skills(skills):
    print(f'Из {len(skills)} скиллов, самыми популярными являются:')
    for index in range(len(d := sorted(skills.items(), key=lambda pair: pair[1], reverse=True))):
        if index == 10:
            break
        count = d[index][1]
        last_word = 'раз'
        if count % 10 == 1:
            last_word = 'раз'
        elif count % 10 in [2, 3, 4]:
            last_word = 'раза'
        print(f'    {index + 1}) {d[index][0]} - упоминается {d[index][1]} {last_word}')


def print_areas(areas):
    print(f'Из {len(areas)} городов, самые высокие средние ЗП:')
    for index in range(len(area := sorted(areas.items(), key=lambda pair: sum(pair[1]) // len(pair[1]), reverse=True))):
        if index == 10:
            break
        salary = area[index][1][0]
        last_word = 'рублей'
        if salary % 10 == 1:
            last_word = 'рубль'
        elif salary % 10 in [2, 3, 4]:
            last_word = 'рубля'
        print(f'    {index + 1}) {area[index][0]} - средняя зарплата {int(salary)} {last_word} (1 вакансия)')


file_name = input()

with open(file_name, encoding='utf-8-sig') as file:
    file_reader = csv.reader(file, delimiter=',')
    flag = True
    titles = []
    rows = []
    for row in file_reader:
        if flag:
            titles = row
            flag = False
            continue
        if '' not in row and len(row) == len(titles):
            rows.append(row)

dicts = []
for row in rows:
    data = {}
    for i in range(len(titles)):
        data[titles[i]] = format_string(row[i])
    data['salary'] = (float(data['salary_to']) + float(data['salary_from'])) // 2
    dicts.append(data)

lowest_salaries = sorted(dicts, key=lambda dictionary: dictionary['salary'])
print(lowest_salaries[:11])
highest_salaries = sorted(dicts, key=lambda dictionary: dictionary['salary'], reverse=True)

skills = {}
for dictionary in dicts:
    for skill in dictionary['key_skills'].split(','):
        skill = skill.strip()
        if skill not in skills.keys():
            skills[skill] = 1
        else:
            skills[skill] += 1


areas = {}
for d in dicts:
    area = d['area_name']
    if area not in areas.keys():
        areas[area] = [d['salary']]
    else:
        areas[area].append(d['salary'])

print_salaries('высокие', highest_salaries)
print()
print_salaries('низкие', lowest_salaries)
print()
print_skills(skills)
print()
print_areas(areas)
