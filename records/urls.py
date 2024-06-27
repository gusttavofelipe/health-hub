from django.urls import path
from records.views import HomeView


app_name = "products"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]
