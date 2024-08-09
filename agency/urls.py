from django.urls import path

from agency.views import index, TopicsListView, NewspaperListView


urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicsListView.as_view(), name="topic-list"),
    path("newspapers/", NewspaperListView.as_view(), name="newspaper-list"),
]

app_name = "agency"
