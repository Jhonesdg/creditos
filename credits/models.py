from django.db import models

# Create your models here.
from solicitudes.models import CreditRequest
from usuarios.models import Manager


class Credit(models.Model):
    account = models.CharField(max_length=10, verbose_name="Número de cuenta", null=True, blank=True)
    installment_value = models.FloatField(verbose_name="Valor de la cuota")
    date = models.DateTimeField(auto_now_add=True)
    manager = models.ForeignKey(Manager, verbose_name="Aprobado por",null=False)
    request = models.ForeignKey(CreditRequest, verbose_name="Solicitud")

