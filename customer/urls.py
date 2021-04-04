from django.urls import path

from . import views

app_name = 'customer'
urlpatterns = [
  # path('create-customer', views.createCustomer , name='createCustomer'),
  path('get-user', views.getUser , name='getUser'),
  path('update-user', views.updateUser , name='updateUser'),
  path('update-password', views.updatePassword , name='updatePassword'),
]