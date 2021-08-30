from demo_calendar_endpoint.models import CompanyStaff
from rest_framework import serializers


class StaffDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyStaff
        fields = '__all__'