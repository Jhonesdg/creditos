from django.db import models
from django.contrib.auth.models import User


class Consultant(User):
    def __str__(self):
        return str(self.first_name)

class Client(User):
    USERNAME_FIELD = 'email'
    def __str__(self):
        return str(self.first_name)

class Manager(User):
    def __str__(self):
        return str(self.first_name)