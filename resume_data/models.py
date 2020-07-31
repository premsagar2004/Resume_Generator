from django.db import models
from django.contrib.auth.models import User


class JsonData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    file = models.FileField(default='document.json', upload_to='userResume/')

    def __str__(self):
        return self.user.username+"'s Resume Json File"

class Contact(models.Model):
    msg_id=models.AutoField(primary_key="True")
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50,default="")
    phone=models.CharField(max_length=50,default="")
    desc=models.CharField(max_length=500,default="")

    def __str__(self):
        return self.name

