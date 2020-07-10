from django.db import models

from clients.models import Client
from core.models import TimeStampedModel, Active


class Estimate(Active, TimeStampedModel):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('sent', 'Sent'),
        ('accept', 'Accept'),
        ('declined', 'Declined'),
        ('invoiced', 'Invoiced'),
        ('revised', 'Revised'),
    )

    client = models.ForeignKey(Client, blank=True, null=True,
                               on_delete=models.CASCADE)
    status = models.CharField(max_length=10, default='open')
    validate = models.DateField()

    def total(self):
        items = self.estimateitem_set.all()
        total = 0
        for item in items:
            total = total + item.quantity * item.unity_price
        return total

    def __str__(self):
        return f"{self.id} - {self.client}"

    class Meta:
        ordering = ('client', 'validate', 'status')
        verbose_name = 'Orçamento'
        verbose_name_plural = 'Orçamentos'


class EstimateItem(Active, TimeStampedModel):
    estimate = models.ForeignKey(Estimate, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    quantity = models.IntegerField(default=1)
    unity_price = models.DecimalField(max_digits=16, decimal_places=2)

    def subtotal(self):
        return self.quantity * self.unity_price

    def __str__(self):
        return f"{self.name} - {self.description}"

    class Meta:
        ordering = ('name', 'description')
        verbose_name = 'Item do orçamento'
        verbose_name_plural = 'Itens do orçamento'
