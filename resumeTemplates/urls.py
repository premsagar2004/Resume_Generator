from django.urls import path
from . import views

urlpatterns = [
    path('', views.templates, name='resumeTemplates'),
    path('', views.res_templates, name='resumeTemplates2')
]
