from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import HealthFacilities


class HealthFacilitiesSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = HealthFacilities
        geo_field = "geom"
        fields = "__all__"