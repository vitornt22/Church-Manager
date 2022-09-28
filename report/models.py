import datetime

from church.models import Church
from django.db import models


# Create your models here.s
class Report(models.Model):
    id = models.BigAutoField(primary_key=True)
    church = models.ForeignKey(Church, on_delete=models.CASCADE)
    mounth = models.CharField(max_length=2, null=False, blank=False)
    year = models.CharField(max_length=4, null=False, blank=False)
    pdfReport = models.FileField(upload_to=str(
        datetime.date.today().year)+'-reports', blank=True)
