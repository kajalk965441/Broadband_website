from import_export import resources
from .models import pricemodel

class PersonResource(resources.ModelResource):
    class Meta:
        model = pricemodel