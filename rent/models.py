from django.db import models


class Rent(models.Model):
    location = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    beforeDate = models.DateTimeField('beforeDate')
    afterDate = models.DateTimeField('afterDate')