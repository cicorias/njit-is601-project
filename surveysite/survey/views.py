from django.http import (HttpResponse,
                         HttpRequest,
                         Http404,
                         HttpResponseRedirect,
                         JsonResponse)

from django.shortcuts import render
from django.urls import reverse

from .models import Survey

from django.views.generic import ListView


class SurveyList(ListView):
    paginate_by = 2
    model = Survey


# def index2(request: HttpRequest) -> HttpResponse:
#     return SurveyList()

def index(request: HttpRequest) -> HttpResponse:
    surveys = Survey.objects.all()
    context = {'items': surveys}

    return render(request, 'survey/index.html', context)
    