from django.shortcuts import render
from rest_framework import generics

from demo_calendar_endpoint.models import CompanyStaff
from demo_calendar_endpoint.serializers import StaffDetailSerializer

class StaffDetailView(generics.RetrieveAPIView):
    queryset = CompanyStaff.objects.all()
    serializer_class = StaffDetailSerializer
    lookup_field = 'username'
