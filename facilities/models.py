from django.contrib.gis.db import models


# Create your models here.
class HealthFacilities(models.Model):
    name = models.CharField(max_length=120, null=True)
    healthcare = models.CharField(max_length=120, null=True)
    amenity = models.CharField(max_length=80, null=True)
    operatory = models.CharField(max_length=80, null=True)
    geom = models.MultiPointField(srid=4326)


class Meta:
    indexes=[
        models.Index(fields=['geom'], name='geom_index')
    ]

def __str__(self):
    return self.name


# Auto-generated `LayerMapping` dictionary for HealthFacilities model
# healthfacilities_mapping = {
#     'name': 'name',
#     'healthcare': 'healthcare',
#     'amenity': 'amenity',
#     'operatory': 'operatory',
#     'geom': 'POINT',
# }
