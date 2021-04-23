from django.urls import path

from . import views

app_name = 'customer'
urlpatterns = [
  path('get-user', views.getUser , name='getUser'),
  path('update-user', views.updateUser , name='updateUser'),
  path('history', views.getReportBikerLog , name='getReportBikerLog'),
]