from django.urls import path
from professional.views import ProfessionalCreateView


app_name = "professionals"

urlpatterns = [
    path("professionals/register/", ProfessionalCreateView.as_view(), name="register"),
]
