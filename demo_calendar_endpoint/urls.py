from django.urls import path

from demo_calendar_endpoint.views import StaffDetailView

urlpatterns = [
    path('<username>/', StaffDetailView.as_view()),
]