from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),

    path("contact/",views.contact,name="ContactUs"),
    path("about/",views.about,name="AboutUs"),
    path("createresume/",views.createresume,name='createResume'),
    path("createresume/templates/",views.templates,name='templates'),
    path("createresume/templates/preview1",views.load_json_table_format,name='preview1'),
    path("createresume/templates/preview2",views.preview2,name='preview2'),

    # path('pdfview1/', views.load_json_table_format, name='view1'),
    path('pdf1/', views.GeneratePdf1.as_view(), name='pdf1'),

    # path('preview2/', views.preview2, name='view2'),
    path('pdf2/', views.GeneratePdf2.as_view(), name='pdf2'),



]

