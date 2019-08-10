from django.db import models
from django.contrib import admin
# Create your models here.
class Sign(models.Model):
    user_id = models.CharField(max_length = 20)
    user_psd = models.CharField(max_length = 20)
    def __str__(self):
        return self.user_id
class SignAdmin(admin.ModelAdmin):
    list_display = ('id','user_id')
class ContractUs(models.Model):
    user_name = models.CharField(max_length=5)
    user_email = models.EmailField(max_length=30)
    user_subject = models.CharField(max_length=30)
    user_message = models.TextField(max_length=800)
    def __str__(self):
        return self.user_name
