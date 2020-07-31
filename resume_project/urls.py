from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.conf.urls.static import static, settings

#django admin Header customization
admin.site.site_header= "Resume Generator(Admin Panel)"
admin.site.site_title= "Welcome to Resume Generator Dashboard"
admin.site.index_title= "Welcome to ResumeGenerator"

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('accounts/', include('accounts.urls')),
    path('', include('resume_data.urls')),
    path('templates/', include('resumeTemplates.urls')),
    path('api-auth/', include('rest_framework.urls'))
    
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
