from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class Host(models.Model):

    id = models.AutoField(primary_key=True, unique=True)
    user = models.CharField(max_length=20)
    host_ip = models.CharField(max_length=20)
    port = models.IntegerField(default=22)
    password = models.CharField(max_length=200)
    default_path = models.CharField(max_length=200)
    


