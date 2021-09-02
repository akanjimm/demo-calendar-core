from django.shortcuts import render
from rest_framework import generics, response, status

from demo_calendar_endpoint.models import CompanyStaff
from demo_calendar_endpoint.serializers import StaffDetailSerializer


class StaffCreateView(generics.GenericAPIView):
    serializer_class = StaffDetailSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        return response.Response(user_data, status=status.HTTP_201_CREATED)


class StaffDetailView(generics.RetrieveAPIView):
    queryset = CompanyStaff.objects.all()
    serializer_class = StaffDetailSerializer
    lookup_field = 'username'


