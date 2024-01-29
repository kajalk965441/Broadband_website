from django.contrib import admin
from .models import contact, servicesmodel, pricemodel
from import_export.admin import ImportExportModelAdmin

class PriceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        list_display= ['price', 'offer']


# class Adminpricemodel(admin.ModelAdmin):
#     list_display= ['price', 'offer']

class Adminservice(ImportExportModelAdmin, admin.ModelAdmin):
    list_display= ['title', 'desc']
    
class Admincontact(ImportExportModelAdmin, admin.ModelAdmin):
    list_display= ['name', 'address', 'city', 'state']
    
    
admin.site.register(contact, Admincontact)
admin.site.register(servicesmodel, Adminservice)
admin.site.register(pricemodel, PriceAdmin)

# Register your models here.
