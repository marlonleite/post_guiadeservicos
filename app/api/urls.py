from django.urls import path, re_path

from . import views

app_name = "api"

urlpatterns = [
   # re_path(r'(?P<key>[-\w+\d+]+)/$', views.index, name='index'),
   path('', views.index, name='index')
]
