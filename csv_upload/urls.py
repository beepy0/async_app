from django.urls import path

from . import views

app_name='csv_upload'
urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_csv, name='upload_csv'),
]
