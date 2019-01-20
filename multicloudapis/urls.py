from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^uploadfile_gcp/', views.uploadfile_gcp, name='gcp'),
    url(r'^uploadfile_azure/', views.uploadfile_azure, name='azure'),
    url(r'^uploadfile_aws/', views.uploadfile_aws, name='aws'),
    url(r'', views.home, name="home"),
    url(r'^uploadchunk_universal/', views.home, name='upload'),

    url(r'^download_universal/', views.universal_download, name='download'),

]
