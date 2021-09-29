from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.IntegerField(default=000000000)
    def full_name(self):
        return self.first_name + ' ' + self.last_name