from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import *


@csrf_exempt
def add_user(request):
    try:
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        age = data.get('age')
        email = data.get('email')
        password = data.get('password')

        user = MyUser()

        user.first_name = first_name
        user.last_name = last_name

        if MyUser.verify_age(age):
            user.age = int(age)
        else:
            return render(request, 'error.html', {'error': 'Age must be greater than 18 and lower than 150!'})

        user.email = email
        user.password = MyUser.hash_password(password)

        user.save()

        saved_user = MyUser.objects.get(email=email)

        return render(request, 'answer.html', {'answer': saved_user.id})

    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


@csrf_exempt
def delete_user(request):
    try:
        data = request.POST
        email = data.get('email')
        password = data.get('password')

        user = MyUser.objects.get(email=email)

        if user.verify_password(password):
            user.delete()
            return render(request, 'answer.html', {'answer': True})
        else:
            return render(
                request,
                'error.html',
                {'error': 'Wrong password'})

    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


@csrf_exempt
def authorise(request):
    try:
        data = request.POST
        email = data.get('email')
        password = data.get('password')

        user = MyUser.objects.get(email=email)
        if user.verify_password(password):
            return render(request, 'user_info.html', {'user': user, 'skills': user.skills})
        else:
            return render(
                request,
                'error.html',
                {'error': 'Wrong password'})
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


@csrf_exempt
def add_vacancy(request):
    try:
        data = request.POST
        name = data.get('name')
        salary = int(data.get('salary'))
        area_name = data.get('area_name')

        vacancy = Vacancy()

        vacancy.name = name
        vacancy.salary = salary
        vacancy.area_name = area_name

        vacancy.save()

        saved_vacancy = Vacancy.objects.get(name=name, salary=salary, area_name=area_name)

        return render(request, 'answer.html', {'answer': saved_vacancy.id})
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


@csrf_exempt
def get_vacancy(request):
    try:
        vacancy_id = request.GET.get('id')

        vacancy = Vacancy.objects.get(id=vacancy_id)

        return render(request, 'vacancy.html', {
            'vacancy': vacancy,
            'skills': vacancy.skills,
            'responses': UserResponse.objects.filter(vacancy=vacancy)
        })
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


@csrf_exempt
def delete_vacancy(request):
    try:
        data = request.POST
        vacancy_id = data.get('id')

        vacancy = Vacancy.objects.get(id=vacancy_id)
        vacancy.delete()
        return render(request, 'answer.html', {'answer': True})
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


@csrf_exempt
def add_skill(request):
    try:
        data = request.POST
        name = data.get('name')

        skill = Skill()
        skill.name = name

        skill.save()

        saved_skill = Skill.objects.get(name=name)

        return render(request, 'answer.html', {'answer': saved_skill.id})
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


@csrf_exempt
def get_skill(request):
    try:
        skill_id = request.GET.get('id')
        skill = Skill.objects.get(id=skill_id)
        return render(request, 'answer.html', {'answer': skill.id})
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


@csrf_exempt
def delete_skill(request):
    try:
        data = request.POST
        skill_id = data.get('id')
        skill = Skill.objects.get(id=skill_id)
        skill.delete()
        return render(request, 'answer.html', {'answer': True})
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


@csrf_exempt
def add_skill_to_vacancy(request):
    try:
        data = request.POST
        vacancy_id = data.get('vacancy')
        skill_id = data.get('skill')

        vacancy = Vacancy.objects.get(id=vacancy_id)
        skill = Skill.objects.get(id=skill_id)

        vacancy_skill = VacancySkill()
        vacancy_skill.vacancy = vacancy
        vacancy_skill.skill = skill

        vacancy_skill.save()

        return render(request, 'answer.html', {'answer': True})
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


@csrf_exempt
def remove_skill_from_vacancy(request):
    try:
        data = request.POST
        vacancy_id = data.get('vacancy')
        skill_id = data.get('skill')

        vacancy = Vacancy.objects.get(id=vacancy_id)
        skill = Skill.objects.get(id=skill_id)

        vacancy_skill = VacancySkill.objects.get(vacancy=vacancy, skill=skill)
        vacancy_skill.delete()

        return render(request, 'answer.html', {'answer': True})
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


@csrf_exempt
def add_skill_to_user(request):
    try:
        data = request.POST
        user_id = data.get('user')
        skill_id = data.get('skill')

        user = MyUser.objects.get(id=user_id)
        skill = Skill.objects.get(id=skill_id)

        user_skill = UserSkill()
        user_skill.user = user
        user_skill.skill = skill

        user_skill.save()

        user_skill.save()

        return render(request, 'answer.html', {'answer': True})
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


@csrf_exempt
def remove_skill_from_user(request):
    try:
        data = request.POST
        user_id = data.get('user')
        skill_id = data.get('skill')

        user = MyUser.objects.get(id=user_id)
        skill = Skill.objects.get(id=skill_id)

        user_skill = UserSkill.objects.get(user=user, skill=skill)
        user_skill.delete()

        return render(request, 'answer.html', {'answer': True})
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


@csrf_exempt
def add_response(request):
    try:
        data = request.POST
        user_id = data.get('user')
        vacancy_id = data.get('vacancy')
        message = data.get('message')

        user = MyUser.objects.get(id=user_id)
        vacancy = Vacancy.objects.get(id=vacancy_id)

        user_response = UserResponse()
        user_response.user = user
        user_response.vacancy = vacancy
        user_response.message = message

        user_response.save()

        saved_user_response = UserResponse.objects.get(user=user, vacancy=vacancy, message=message)

        return render(request, 'answer.html', {'answer': saved_user_response.id})
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


@csrf_exempt
def get_response(request):
    try:
        data = request.POST
        user_response_id = data.get('id')

        user_response = UserResponse.objects.get(id=user_response_id)

        return render(request, 'answer.html', {'answer': user_response.message})
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})


@csrf_exempt
def delete_response(request):
    try:
        data = request.POST
        user_response_id = data.get('id')

        user_response = UserResponse.objects.get(id=user_response_id)
        user_response.delete()

        return render(request, 'answer.html', {'answer': True})
    except Exception as e:
        return render(request, 'error.html', {'error': str(e)})

