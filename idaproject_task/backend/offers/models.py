from statistics import mode
from django.db import models

# Create your models here.
class Offer(models.Model):
    bank_name = models.CharField(max_length=120)
    term_min = models.IntegerField(default=10)
    term_max = models.IntegerField(default=30)
    rate_min = models.DecimalField(decimal_places=1, default=1.8, max_digits=4)
    rate_max = models.DecimalField(decimal_places=1, default=9.8, max_digits=4)
    payment_min = models.IntegerField(default=1000000)
    payment_max = models.IntegerField(default=10000000)
