from django.urls import path
from records.views import HomeView


app_name = "records"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]
