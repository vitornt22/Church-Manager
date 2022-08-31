
from church.models import Church
from django.db import models
from django.utils.text import slugify

ESTADOS = (('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'),  # noqa
           ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('PI', 'PI'),  # noqa
            ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'),  # noqa
           ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO'))

GENRE = (('F', 'FEMININO'), ('M', 'MASCULINO'))
# Create your models here.


class Member (models.Model):
    fullName = models.CharField(null=False, blank=False, max_length=100)
    cpf = models.CharField(null=False, blank=False, max_length=15, unique=True)
    adress = models.CharField(null=True, blank=True, max_length=50)
    phone = models.CharField(max_length=15)
    church = models.ForeignKey(
        Church, blank=True, null=True, on_delete=models.CASCADE)
    born = models.DateField(default=None)
    email = models.EmailField(blank=True, null=True, unique=True)
    number = models.IntegerField()
    city = models.CharField(blank=True, null=True, max_length=100)
    state = models.CharField(blank=True, null=True, max_length=2, choices=ESTADOS)  # noqa
    genre = models.CharField(blank=True, null=True, max_length=1, choices=GENRE)  # noqa
    district = models.CharField(blank=True, null=True, max_length=30)
    slug = models.SlugField(unique=True)
    is_baptized_water = models.BooleanField(
        default=False)
    is_baptized_holySpirit = models.BooleanField(
        default=False)
    is_tither = models.BooleanField(default=False)

    upload = models.ImageField(blank=True, null=True, upload_to='uploads/')

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.cpf)}'
            self.slug = slug

        return super().save(*args, **kwargs)
