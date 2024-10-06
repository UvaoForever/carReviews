from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField(max_length=40)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE, null=True)

class Producer(models.Model):
    name = models.CharField(max_length=40)
    country = models.ForeignKey(Country, related_name="producers", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE, null=True)

class Auto(models.Model):
    name = models.CharField(max_length=30)
    producer = models.ForeignKey(Producer, related_name="autos", on_delete=models.CASCADE)
    start_year = models.PositiveSmallIntegerField()
    end_year = models.PositiveSmallIntegerField(null=True)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE, null=True)

class Comment(models.Model):
    email = models.EmailField()
    auto = models.ForeignKey(Auto, related_name="comments", on_delete=models.CASCADE)
    date_comment = models.DateField()
    comment = models.TextField()
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE, null=True)