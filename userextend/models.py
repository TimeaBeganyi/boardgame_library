from django.contrib.auth.models import User
from django.db import models


class UserExtend(User):
    gender_option = (('male', 'Male'), ('female', 'Female'), ('other', 'Other'))

    date_of_birth = models.DateField()
    email_confirmation = models.EmailField(max_length=100)
    gender = models.CharField(max_length=6, choices=gender_option)
    phone_number = models.CharField(max_length=14)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
