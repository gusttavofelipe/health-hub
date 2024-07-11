from django.urls import path
from professional.views import (
    ProfessionalCreateView,
    ProfessionalLoginView,
    ProfessionalLogoutView,
)


app_name = "professionals"

urlpatterns = [
    path("professionals/register/", ProfessionalCreateView.as_view(), name="register"),
    path("professionals/login/", ProfessionalLoginView.as_view(), name="login"),
    path("professionals/logout/", ProfessionalLogoutView.as_view(), name="logout"),
]
