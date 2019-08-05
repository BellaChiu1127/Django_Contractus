from django.contrib import admin
from .models import Sign,SignAdmin,ContractUs

# Register your models here.
admin.site.register(Sign,SignAdmin)
admin.site.register(ContractUs)