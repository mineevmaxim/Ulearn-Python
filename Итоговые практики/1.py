from django.db import models
import hashlib
import datetime


class MyUser(models.Model):
    first_name = models.CharField("Имя", max_length=64)
    last_name = models.CharField('Фамилия', max_length=64)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    password = models.CharField('Пароль', max_length=64)
    skills_list = []

    class Meta:
        db_table = "my_user"

    def get_name(self):
        return f'{self.last_name} {self.first_name}'

    @staticmethod
    def hash_password(password):
        return hashlib.sha1(password.encode()).hexdigest()

    def verify_password(self, password):
        return self.password == hashlib.sha1(password.encode()).hexdigest()

    @staticmethod
    def verify_age(age):
        return 18 <= int(age) <= 150

    @property
    def skills(self):
        return [
            user_skill.skill.name for user_skill in UserSkill.objects.filter(user=self)
        ]


class Vacancy(models.Model):
    name = models.TextField()
    salary = models.IntegerField()
    area_name = models.TextField()
    created_at = models.DateTimeField(default=datetime.datetime.now)
    skills_list = []

    @property
    def skills(self):
        return [
            vacancy_skill.skill.name for vacancy_skill in VacancySkill.objects.filter(vacancy=self)
        ]

    class Meta:
        db_table = 'vacancy'


class Skill(models.Model):
    name = models.CharField("Имя", max_length=64)

    class Meta:
        db_table = 'skill'


class VacancySkill(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    class Meta:
        db_table = 'vacancy_skill'
        unique_together = ('vacancy', 'skill')


class UserSkill(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_skill'
        unique_together = ('user', 'skill')


class UserResponse(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    message = models.TextField()

    class Meta:
        db_table = 'user_response'
