# MY_PROJECT/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_all.urls')),  
]

handler404 = 'app_all.views.error_404_view'
