from django.shortcuts import render
from rest_framework import viewsets
from .models import HealthFacilities
from .serializers import HealthFacilitiesSerializer
# Create your views here.

class HealthFacilitiesViewSet(viewsets.ModelViewSet):
    queryset = HealthFacilities.objects.all()
    serializer_class = HealthFacilitiesSerializer