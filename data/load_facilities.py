import os
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.gdal import DataSource

from facilities.models import HealthFacilities


# Auto-generated `LayerMapping` dictionary for HealthFacilities model
healthfacilities_mapping = {
    'name': 'name',
    'healthcare': 'healthcare',
    'amenity': 'amenity',
    'operatory': 'operatory',
    'geom': 'MULTIPOINT',
}

def import_data(verbose=True):
    file = os.getcwd() + '/data/health_facilities.gpkg'
    data_source = DataSource(file)
    facilities_layer = data_source[0].name

    facilities_layer_mapping = LayerMapping(
        HealthFacilities, file, healthfacilities_mapping, layer=facilities_layer
    )

    facilities_layer_mapping.save(strict=True, verbose=verbose)