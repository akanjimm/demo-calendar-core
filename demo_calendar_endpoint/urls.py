from django.urls import path

from demo_calendar_endpoint.views import StaffDetailView, StaffCreateView

urlpatterns = [
    path('create/', StaffCreateView.as_view()),
    path('<username>/', StaffDetailView.as_view()),
]