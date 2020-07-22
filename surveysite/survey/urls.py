from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='survey-index'),  # views.SurveyList.as_view())  # 
    path('foo/', views.SurveyList.as_view())
]
