from django.db import models


# Create your models here.
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=128)

    class Meta:
        db_table = 'user'
