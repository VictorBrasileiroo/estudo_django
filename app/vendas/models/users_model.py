from django.db import models

class UserModel(models.Model):
    username = models.CharField(max_length=50)
    adress = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username