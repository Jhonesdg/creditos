from django.db import models

# Create your models here.
from usuarios.models import Client


class TypeCredit(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nombre", null=False, blank=False)
    rate = models.FloatField(verbose_name="Tasa", null=False)

    def __str__(self):
        return self.name


class CreditRequest(models.Model):
    INSTALLMENTS = (
        (6, 6),
        (12, 12),
        (24, 24),
        (36, 36),
    )
    STATUS = (
        (0, "Creada"),
        (1, "Evaluada"),
        (2, "Aprobada"),
        (3, "Rechazada"),
    )
    client = models.ForeignKey(Client, verbose_name="Cliente", null=False, blank=False)
    amount = models.CharField(max_length=255, verbose_name="Monto", null=False, blank=False)
    installments = models.IntegerField(choices=INSTALLMENTS, verbose_name="Cuotas", default=6,max_length=2)
    description = models.TextField(max_length=1500, blank=True)
    status = models.IntegerField(choices=STATUS, verbose_name="Estado", default=0, max_length=2)
    date = models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey(TypeCredit, verbose_name="Tipo de credito", null=False, blank=False)
    observations = models.TextField(max_length=1500, blank=True)

    def __str__(self):
        return str(self.client)


