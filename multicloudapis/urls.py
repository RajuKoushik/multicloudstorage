from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^uploadfile_gcp/', views.uploadfile_gcp, name='project_list'),


]