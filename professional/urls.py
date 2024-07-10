from django.urls import path
from professional.views import ProfessionalCreateView, ProfessionalLoginView


app_name = "professionals"

urlpatterns = [
    path("professionals/register/", ProfessionalCreateView.as_view(), name="register"),
    path("professionals/login/", ProfessionalLoginView.as_view(), name="login"),
]
