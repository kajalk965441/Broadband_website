from django.db import models

# Create your models here.(models)
class contact(models.Model):
    name= models.CharField(max_length=200, blank=True)
    address=models.CharField( max_length=200, blank=True)
    city=models.CharField(max_length=200, blank=True)
    state= models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class servicesmodel(models.Model):
    title=models.CharField(max_length=100)
    desc = models.TextField(max_length=250)


class pricemodel(models.Model):
    price= models.CharField(max_length=100, verbose_name="model verbose name")
    offer= models.CharField(max_length=100)

# class Excelfileupload(models.Model):
#     excel_file_upload = models.FileField(upload_to="excel")