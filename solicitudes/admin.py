from django.contrib import admin

# Register your models here.
from .models import TypeCredit,CreditRequest
admin.site.register(TypeCredit)
admin.site.register(CreditRequest)