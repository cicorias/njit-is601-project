from django.urls import path

from . import views

urlpatterns = [
    #  this is an alternate view of survye list.
    path('alt/', views.index, name='survey-index'),
    #  this uses django feature for pagination.
    path('', views.SurveyList.as_view()),
    path('<int:item_id>/', views.detail, name='survey-detail'),
]
