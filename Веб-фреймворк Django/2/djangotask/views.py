from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import *

fake_data = [
    {'name': 'Студент', 'salary': '3000', 'area_name': 'Екатеринбург', 'published_at': '2023-07-23 19:04:12+05:00'},
    {'name': 'Django разработчик', 'salary': '300000', 'area_name': 'Москва',
     'published_at': '2023-07-20 16:19:56+03:00'},
    {'name': '...', 'salary': '...', 'area_name': '...', 'published_at': '...'}]


@csrf_exempt
def hello(request):
    # TODO: получить имя пользователя из таблицы site_users по полученному id из POST запроса

    return render(request, 'hello.html', {'name': 'Поменяй меня'})


def all_vacancies(request):
    # TODO: получить все данные о вакансиях из таблицы vacancies

    return render(request, 'vacancies_table.html', {'data': fake_data})


def filter_vacancies(request):
    # TODO: получить данные о вакансиях из таблицы vacancies с учетом фильтров из GET запроса

    return render(request, 'vacancies_table.html', {'data': fake_data})


def get_salary_year_dynamic(request):
    # TODO: получить динамику уровня зарплат по годам из таблицы vacancies

    fake_dynamic = [{'first': '151500', 'second': '2023'}, {'first': '...', 'second': '...'}, ]

    return render(request, 'dynamics_table.html',
                  {'first_parameter': 'Avg salary', 'second_parameter': 'Year', 'data': fake_dynamic})


def get_count_year_dynamic(request):
    # TODO: получить динамику количества вакансий по годам из таблицы vacancies

    fake_dynamic = [{'first': '2', 'second': '2023'}, {'first': '...', 'second': '...'}, ]

    return render(request, 'dynamics_table.html',
                  {'first_parameter': 'Vacancies count', 'second_parameter': 'Year', 'data': fake_dynamic})


def get_top_10_salary_city(request):
    # TODO: получить уровень зарплат по городам (в порядке убывания) - только первые 10 значений

    fake_dynamic = [{'first': '300000', 'second': 'Москва'},
                    {'first': '3000', 'second': 'Екатеринбург'},
                    {'first': '...', 'second': '...'}, ]

    return render(request, 'dynamics_table.html',
                  {'first_parameter': 'Avg salary', 'second_parameter': 'City', 'data': fake_dynamic})


def get_top_10_vac_city(request):
    # TODO: получить долю вакансий по городам (в порядке убывания) - только первые 10 значений

    fake_dynamic = [{'first': '0.5', 'second': 'Екатеринбург'},
                    {'first': '0.5', 'second': 'Москва'},
                    {'first': '...', 'second': '...'}, ]

    return render(request, 'dynamics_table.html',
                  {'first_parameter': 'Vacancy rate', 'second_parameter': 'City', 'data': fake_dynamic})
