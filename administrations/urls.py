from django.urls import path

from . import views

app_name = 'administrations'
urlpatterns = [
    path('activate-customer', views.activateCustomer, name='activateCustomer'),
    path('deactivate-customer', views.deactivateCustomer, name='deactivateCustomer'),
    path('activate-biker', views.activateBiker, name='activateBiker'),
    path('deactivate-biker', views.deactivateBiker, name='deactivateBiker'),
    path('list-customer', views.listCustomer, name='listCustomer'),
    path('list-biker', views.listBiker, name='listBiker'),
    path('delete-customer', views.deleteCustomer, name='deleteCustomer'),
    path('delete-biker', views.deleteBiker, name='deleteBiker'),
    path('update-biker', views.updateBiker, name='updateBiker'),
    path('update-customerr', views.updateCustomer, name='updateCustomer'),
    path('get-biker', views.getBiker, name='getBiker'),
    path('get-customer', views.getCustomer, name='getCustomer'),
    path('get-user', views.getUser, name='getUser'),
    path('test-connection', views.testConnection, name='testConnection'),

]
