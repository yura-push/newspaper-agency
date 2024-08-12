from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from agency.models import Topic, Redactor, Newspaper


def index(request: HttpRequest) -> HttpResponse:
    num_topics = Topic.objects.count()
    num_redactors = Redactor.objects.count()
    num_newspapers = Newspaper.objects.count()
    context = {
        "num_topics": num_topics,
        "num_redactors": num_redactors,
        "num_newspapers": num_newspapers
    }
    return render(request, "agency/index.html", context=context)


class TopicsListView(generic.ListView):
    model = Topic
    template_name = "agency/topic_list.html"


class NewspaperListView(generic.ListView):
    model = Newspaper
    queryset = Newspaper.objects.select_related("topic")


class RedactorListView(generic.ListView):
    model = Redactor


class NewspaperDetailView(generic.DetailView):
    model = Newspaper
