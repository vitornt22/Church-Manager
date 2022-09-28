from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.
ESTADOS = (('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'),  # noqa
           ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('PI', 'PI'),  # noqa
            ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'),  # noqa
           ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO'))


class ChurchManager(BaseUserManager):
    def create_user(self, cnpj, name, email, password=None):
        if not name:
            raise ValueError('Nome da Igreja é necessário')
        if not cnpj:
            raise ValueError('CNPJ da Igreja é necessário')
        if not email:
            raise ValueError('Email é necessário')
        if not password:
            raise ValueError('Senha é necessária')

        user = self.model(
            name=name,
            cnpj=cnpj,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, cnpj, password=None):
        user = self.create_user(
            name=name,
            cnpj=cnpj,
            email=email,
            password=password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Church (AbstractBaseUser):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=70, null=False, blank=False)
    ministery = models.CharField(max_length=50)
    email = models.EmailField()
    cnpj = models.CharField(max_length=18)
    phone = models.CharField(max_length=15)
    adress = models.CharField(max_length=60)
    number = models.IntegerField()
    city = models.CharField(max_length=80)
    state = models.CharField(blank=True, null=True, max_length=2, choices=ESTADOS)  # noqa
    district = models.CharField(max_length=40)

    USERNAME_FIELD = 'cnpj'
    REQUIRED_FIELDS = ['name', 'email', 'cnpj', 'password']

    objects = ChurchManager()

    def __str__(self):
        return self.name + '- ' + str(self.cnpj)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
