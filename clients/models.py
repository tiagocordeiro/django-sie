from django.db import models

from core.models import TimeStampedModel, Active


class Client(Active, TimeStampedModel):
    TYPE_CHOICES = (
        ('company', "Company"),
        ('individual', "Individual"),
    )
    name = models.CharField(max_length=50, unique=True)
    type = models.CharField(choices=TYPE_CHOICES, max_length=20)


class Contact(Active, TimeStampedModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    mobile = models.CharField(max_length=20, blank=True)
