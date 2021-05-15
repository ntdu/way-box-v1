from django.urls import path

from . import views

app_name = 'biker'
urlpatterns = [
  path('create-biker', views.createBiker , name='createBiker'),
  path('get-biker', views.getBiker , name='getBiker'),
  path('update-biker', views.updateBiker , name='updateBiker'),
  path('update-password', views.updatePassword , name='updatePassword'),

  path('get-vehicle', views.getVehicle , name='getVehicle'),
  path('create-vehicle', views.createVehicle , name='createVehicle'),
  path('update-vehicle', views.updateVehicle , name='updateVehicle'),
  path('delete-vehicle', views.deleteVehicle , name='deleteVehicle'),

  path('get-detail-biker-log', views.getDetailBikerLog , name='getDetailBikerLog'),
  path('create-review-trip', views.createReviewTrip , name='createReviewTrip'),
]