from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^uploadfile_gcp/', views.uploadfile_gcp, name='gcp'),
    url(r'^uploadfile_azure/', views.uploadfile_azure, name='azure'),
    url(r'^uploadfile_aws/', views.uploadfile_aws, name='aws'),
    url(r'^uploadchunk_gcp/', views.uploadfile_chunk_gcp, name='aws_chunk'),
    url(r'^uploadchunk_universal/', views.universal_uploadfile_chunk, name='aws_universal'),

]
