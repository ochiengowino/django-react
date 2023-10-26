from django.contrib import admin
from .models import HealthFacilities
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
# admin.site.register(HealthFacilities)

class HealthFacilitiesAdmin(LeafletGeoAdmin):
    list_display = ('name','healthcare')
    # pass


admin.site.register(HealthFacilities, HealthFacilitiesAdmin)