from django.contrib import admin

# Register your models here.
from .models import Consultant,Manager,Client
admin.site.register(Consultant)
admin.site.register(Manager)
admin.site.register(Client)