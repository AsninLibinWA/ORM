from django.db import models
from django.contrib import admin
class service_DB(models.Model):
    Vechicle_No=models.CharField()
    Name=models.CharField()
    Address=models.TextField()
    Mobile=models.IntegerField()
    DoB=models.DateField()
    Received_Date=models.DateField()
    Vechicle_Type=models.CharField()
class service_DBAdmin(admin.ModelAdmin):
    list_display=["Vechicle_No","Name","Address","Mobile","DoB","Received_Date","Vechicle_Type"]

 