from xmlrpc.server import SimpleXMLRPCServer
import pandas as pd


def get_vacancy_by_id(id, data):
    return data[id].to_dict()


def get_vacancies_by_city(city, data):
    return data[data['city'] == city]


def get_vacancies_by_min_salary(salary, data):
    ...


def exit_server():
    ...


def format_dict(data):
    names = {
        'name': 'Название вакансии',
        'salary_from': 'Зарплата от',
        'salary_to': 'Зарплата до',
        'city': 'Город',
    }
    return {names[key]: value for (key, value) in data.items()}


def start_server():
    data = pd.read_csv(
        'vacancies.csv',
        names=[
            'name',
            'salary_from',
            'salary_to',
            'currency',
            'city',
            'published_at',
        ]
    )

    server = SimpleXMLRPCServer(("localhost", 8000))
