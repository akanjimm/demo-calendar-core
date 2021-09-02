from demo_calendar_endpoint.models import CompanyStaff
from rest_framework import serializers


class StaffDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyStaff
        fields = '__all__'


    def create(self, validated_data):

        # registering staff detail
        CompanyStaff.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            company_name=validated_data['company_name'],
            department=validated_data['department'],
            role=validated_data['role'],
            is_superadmin=validated_data['is_superadmin'],
            is_admin=validated_data['is_admin'],
            is_employee=validated_data['is_employee']
        )
        return validated_data