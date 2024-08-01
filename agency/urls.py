from django.urls import path

from agency.views import index, TopicsListView


urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicsListView.as_view(), name="topics-list"),
]

app_name = "agency"
