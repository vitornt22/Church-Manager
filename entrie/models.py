
from church.models import Church
from django.db import models

CHOICES = (('oferta', 'Oferta'), ('dizimo', 'Dízimo'))

# Create your models here.


class Entrie(models.Model):
    id = models.BigAutoField(primary_key=True)
    church = models.ForeignKey(
        Church, on_delete=models.CASCADE, null=True, blank=True)
    category = models.CharField(
        choices=CHOICES, max_length=8, blank=False, null=False)
    date = models.DateField(null=True, blank=True)
    value = models.FloatField(blank=False, null=False)
    ocassion = models.CharField(max_length=55, blank=False, null=False)
