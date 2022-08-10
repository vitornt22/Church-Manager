from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from church.models import Church

# Create your models here.



class AccountManager(BaseUserManager):
    def create_user(self, name, email, password=None):
        if not name:
            raise ValueError('Nome da empresa é necessário')
        if not email:
            raise ValueError('Email é necessário')
        if not password:
            raise ValueError('Senha é necessária')

        user = self.model(
            name=name,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password=None):
        user = self.create_user(
            name=name,
            email=email,
            password=password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account (AbstractBaseUser):
    id= models.BigAutoField(primary_key=True)
    name = models.CharField(
        blank=False, null=False, max_length=80)
    email = models.EmailField(blank=False, null=False, unique=True)
    password = models.CharField(
        blank=False, null=False, verbose_name='password', max_length=88, )
    church =  models.ForeignKey(Church, on_delete=models.CASCADE, null=True)
    is_admin = models.BooleanField(blank=True, null=True, default=False)
    is_active = models.BooleanField(blank=True, null=True, default=True)
    is_staff = models.BooleanField(blank=True, null=True, default=False)
    is_superuser = models.BooleanField(blank=True, null=True, default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'password']

    objects = AccountManager()

    def __str__(self):
        return self.name + '- ' + str(self.email)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
