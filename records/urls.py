from django.urls import path
from records.views import (
    HomeView,
    PersonalHealthCreateView,
    PersonalHealthRecordListView,
    PersonalHealthRecordDetailView,
)


app_name = "records"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("records/register/", PersonalHealthCreateView.as_view(), name="register"),
    path("records/list/", PersonalHealthRecordListView.as_view(), name="list-records"),
    path(
        "records/<uuid:uuid>/", PersonalHealthRecordDetailView.as_view(), name="detail"
    ),
]
