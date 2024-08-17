from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from agency.models import Topic, Redactor, Newspaper


def index(request: HttpRequest) -> HttpResponse:
    num_topics = Topic.objects.count()
    num_redactors = Redactor.objects.count()
    num_newspapers = Newspaper.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        "num_topics": num_topics,
        "num_redactors": num_redactors,
        "num_newspapers": num_newspapers,
        "num_visits": num_visits + 1,
    }
    return render(request, "agency/index.html", context=context)


class TopicsListView(generic.ListView):
    model = Topic
    template_name = "agency/topic_list.html"
    paginate_by = 5


class NewspaperListView(generic.ListView):
    model = Newspaper
    queryset = Newspaper.objects.select_related("topic")
    paginate_by = 5


class RedactorListView(generic.ListView):
    model = Redactor
    paginate_by = 5


class NewspaperDetailView(generic.DetailView):
    model = Newspaper


class RedactorDetailView(generic.DetailView):
    model = Redactor
    queryset = Redactor.objects.prefetch_related("newspapers")
