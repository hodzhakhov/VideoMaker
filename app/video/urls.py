from django.contrib import admin
from django.urls import path

from creator.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('runtext', index, name='index'),
]
