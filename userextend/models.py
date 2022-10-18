from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserExtend(User):
    gender_option = (('male', 'Male'), ('female', 'Female'), ('other', 'Other'))

    date_of_birth = models.DateField()
    email_confirmation = models.EmailField(max_length=100)
    gender = models.CharField(max_length=6, choices=gender_option)
    phone_number = models.CharField(max_length=14)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class UserProfile(models.Model):
    user = models.OneToOneField(UserExtend, null=True, on_delete=models.CASCADE)

    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True)
    about = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return f'{self.user.first_name}'
