from django.db import models

class Survey(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    age=models.IntegerField()
    role=models.CharField(max_length=200)
    comments=models.TextField()