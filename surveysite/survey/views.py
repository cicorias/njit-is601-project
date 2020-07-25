from typing import Tuple, Any, Dict
import uuid
from django.http import (HttpResponse,
                         HttpRequest,
                         Http404,
                         HttpResponseRedirect,
                         JsonResponse)

from django.views.generic import ListView, View, TemplateView
from django.shortcuts import get_object_or_404, redirect, render
#  from django.urls import reverse

from .models import Survey, SurveyResponse
# from .forms import ResponseForm


class SurveyList(ListView):
    '''this is the index view for /survey/'''
    paginate_by = 2
    model = Survey


class SurveyView(View):
    def get(self, request: HttpRequest, *args: Tuple, **kwargs: Dict[str, Any]):
        # survey = get_object_or_404(Survey, is_published=True, id=kwargs['item_id'])
        survey = get_object_or_404(Survey, id=kwargs['item_id'])
        context = {
            'response_id': uuid.uuid4().hex,
            'survey': survey,
        }

        return render(request, 'survey/response.html', context)

    def post(self, request: HttpRequest, *args: Tuple, **kwargs: Dict[str, Any]):
        # survey = get_object_or_404(Survey, is_published=True, id=kwargs['item_id'])
        survey = get_object_or_404(Survey, id=kwargs['item_id'])
        session_key = request.session.session_key
        data = request.POST.copy().dict()
        if 'csrfmiddlewaretoken' in data:
            del data['csrfmiddlewaretoken']

        response_id = data['response_id']

        data['session_key'] = session_key
        response = SurveyResponse(
            survey=survey,
            response_id=response_id,
            session_key=session_key,
            content=data
        )
        response.save()

        if response is None:
            #  should never happen....
            return redirect('/')
        else:
            #  TODO: add a url for below...
            return redirect('response-confirm',
                            id=response.id)

        #  return HttpResponse('thanks')


class ResponseConfirm(TemplateView):
    template_name = 'survey/response-confirm.html'

    def get_context_data(self, **kwargs):
        context = super(ResponseConfirm, self).get_context_data(**kwargs)
        response = get_object_or_404(SurveyResponse, id=kwargs['id'])

        context['id'] = kwargs['id']
        context['response'] = response
        return context


def index(request: HttpRequest) -> HttpResponse:
    '''reached via /alt now'''
    surveys = Survey.objects.all()
    context = {'items': surveys}

    return render(request, 'survey/index.html', context)


def detail(request: HttpRequest, item_id: int) -> HttpResponse:
    '''the page to complete the survey with
    url form ./survey/<id>'''
    return HttpResponse('foo')
