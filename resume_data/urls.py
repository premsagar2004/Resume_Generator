from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),

    path('pdfview1/', views.load_json_table_format, name='view1'),
    path('pdf1/', views.GeneratePdf1.as_view(), name='pdf1'),

    path('preview2/', views.preview2, name='view2'),
    path('pdf2/', views.GeneratePdf2.as_view(), name='pdf2'),



]

