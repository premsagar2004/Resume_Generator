from django.db import models
from django.contrib.auth.models import User


class JsonData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    file = models.FileField(default='document.json', upload_to='userResume/')

    def __str__(self):
        return self.user.username+"'s Resume Json File"

