
from church.models import Church
from django.db import models


# Create your models here.
class Spent(models.Model):
    id = models.BigAutoField(primary_key=True)
    church = models.ForeignKey(
        Church, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(null=False, blank=False)
    value = models.FloatField(blank=False, null=False)
    ocassion = models.CharField(max_length=55, blank=False, null=False)
