from django.db import models

from core.models import TimeStampedModel, Active


class Client(Active, TimeStampedModel):
    TYPE_CHOICES = (
        ('company', "Company"),
        ('individual', "Individual"),
    )
    name = models.CharField(max_length=50, unique=True)
    type = models.CharField(choices=TYPE_CHOICES, max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Contact(Active, TimeStampedModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    mobile = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('client', 'name')
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
