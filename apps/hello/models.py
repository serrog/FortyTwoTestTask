from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    date_of_birth = models.DateField()
    bio = models.TextField()
    email = models.EmailField()
    jid = models.CharField(max_length=40)
    skype = models.CharField(max_length=40)
    other = models.TextField()
