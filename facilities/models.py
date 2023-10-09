from django.contrib.gis.db import models


# Create your models here.
class HealthFacilities(models.Model):
    name = models.CharField(max_length=80)
    healthcare = models.CharField(max_length=80)
    amenity = models.CharField(max_length=80)
    operator: type = models.CharField(max_length=80)
    geom = models.PointField(srid=4326)


# Auto-generated `LayerMapping` dictionary for HealthFacilities model
# healthfacilities_mapping = {
#     'name': 'name',
#     'healthcare': 'healthcare',
#     'amenity': 'amenity',
#     'operator:type': 'operator:type',
#     'geom': 'POINT',
# }
