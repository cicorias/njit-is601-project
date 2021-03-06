from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    #  this is an alternate view of survye list.
    path('alt/', views.index, name='survey-index'),
    #  this uses django feature for pagination.
    path('', login_required(views.SurveyList.as_view(
        template_name='survey_list.html'))),
    #  path('<int:item_id>/', views.detail, name='survey-detail'),
    path('<int:item_id>/', views.SurveyView.as_view(),
         name='survey-detail'),
    url(r'^confirm/(?P<id>\w+)/', views.ResponseConfirm.as_view(),
        name='response-confirm'),
]
