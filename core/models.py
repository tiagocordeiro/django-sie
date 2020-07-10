from django.contrib.auth.models import User
from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'criado em',
        auto_now_add=True,
        auto_now=False
    )
    modified = models.DateTimeField(
        'modificado em',
        auto_now_add=False,
        auto_now=True
    )

    class Meta:
        abstract = True


class Active(models.Model):
    active = models.BooleanField('ativo', default=True)

    class Meta:
        abstract = True


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField('Email', unique=True, error_messages={
        'unique': "A user with that email already exists.",
    }, blank=True)
    first_name = models.CharField('Nome', max_length=30, blank=True)
    last_name = models.CharField('Sobrenome', max_length=30, blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=50, blank=True)
    estate = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    postal_code = models.CharField(max_length=10, blank=True)
    about = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='profiles/', blank=True, null=True)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Profiles'


class Company(models.Model):
    name = models.CharField('Nome', max_length=50)
    address = models.CharField('Endereço', max_length=100)
    phone = models.CharField('Telefone', max_length=20)
    website = models.URLField('Website')
    facebook = models.URLField('Facebook')
    instagram = models.URLField('Instagram')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Informações da Empresa'
        verbose_name_plural = 'Informações da Empresa'
