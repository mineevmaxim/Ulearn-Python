import json
import re

from bs4 import BeautifulSoup


def parse_salary(salary, exchange):
    currency = exchange['₽']

    for curr in exchange.keys():
        if curr in salary:
            currency = exchange[curr]

    salary = re.sub(r"\s+", "", salary)

    if (text := re.findall(r'\d+', salary)) == 2:
        return f'{str(float(text[0]) * currency)}-{str(float(text[1]) * currency)}'
    else:
        return str(float(text[0]) * currency)


exchange = {
    '₽': 1.0,
    '$': 100.0,
    '€': 105.0,
    '₸': 0.210,
    'Br': 30.0,
}

html = input()
file = open(html)
soup = BeautifulSoup(file, features="html.parser")
result = {'vacancy': soup.find(class_='bloko-header-section-1').text}

salary = soup.find(class_='bloko-header-section-2_lite').text
result['salary'] = parse_salary(salary, exchange)

experience = soup.find(attrs={'data-qa': 'vacancy-experience'}).text.replace("–","-")
experience = re.findall(r'\d+-\d+', experience)
if len(experience) == 0:
    experience = None
else:
    experience = experience[0]

result['experience'] = experience

company = soup.find('span', {"class":"vacancy-company-name"}).text
result['company'] = company

description = soup.find('div', {"class":"g-user-content"}).text
result['description'] = description

skills = soup.find(class_='bloko-tag-list').findAll(class_='bloko-tag__section')
result['skills'] = ', '.join([x.text for x in skills])

created_at = soup.find(class_='vacancy-creation-time-redesigned').span.text
result['created_at'] = created_at

print(json.dumps(result))