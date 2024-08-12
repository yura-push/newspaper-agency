from django.urls import path

from agency.views import (
    index,
    TopicsListView,
    NewspaperListView,
    RedactorListView,
    NewspaperDetailView,
)


urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicsListView.as_view(), name="topic-list"),
    path("newspapers/", NewspaperListView.as_view(), name="newspaper-list"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("newspapers/<int:pk>/", NewspaperDetailView.as_view(), name="newspaper-detail"),
]

app_name = "agency"
