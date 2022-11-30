from django.db import models
from datetime import date
# Create your models here.


class Task(models.Model):
    user = models.CharField(default="", max_length=200)
    vendor = models.CharField(default="", max_length=200)
    category = models.CharField(default="", max_length=200)
    date = models.DateField(default=date.today().strftime(
        "%Y-%m-%d"), blank=True, null=True)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=False, blank=False)
    objects = models.Manager()

    def __str__(self):
        return self.user
