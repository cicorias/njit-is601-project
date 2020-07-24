from typing import Tuple, Any, Dict
import uuid
from django.http import (HttpResponse,
                         HttpRequest,
                         Http404,
                         HttpResponseRedirect,
                         JsonResponse)

from django.views.generic import ListView, View
from django.shortcuts import get_object_or_404, render
#  from django.urls import reverse

from .models import Survey, SurveyResponse
# from .forms import ResponseForm


class SurveyList(ListView):
    '''this is the index view for /survey/'''
    paginate_by = 2
    model = Survey


class SurveyView(View):
    def get(self, request: HttpRequest, *args: Tuple, **kwargs: Dict[str, Any]):
        survey = get_object_or_404(Survey, is_published=True, id=kwargs['item_id'])

        #  form = ResponseForm()

        context = {
            'response_id': uuid.uuid4().hex,
            'survey': survey,
        }

        return render(request, 'survey/response.html', context)

    def post(self, request: HttpRequest, *args: Tuple, **kwargs: Dict[str, Any]):
        survey = get_object_or_404(Survey, id=kwargs['item_id'])
        response = SurveyResponse(
            survey=survey,
            content='againfoo'
        )
        response.save()

        return HttpResponse('thanks')


# def index2(request: HttpRequest) -> HttpResponse:
#     return SurveyList()

def index(request: HttpRequest) -> HttpResponse:
    '''reached via /alt now'''
    surveys = Survey.objects.all()
    context = {'items': surveys}

    return render(request, 'survey/index.html', context)


def detail(request: HttpRequest, item_id: int) -> HttpResponse:
    '''the page to complete the survey with
    url form ./survey/<id>'''
    return HttpResponse('foo')
