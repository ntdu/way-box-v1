from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('customer.urls')),
    path('biker/', include('biker.urls')),
    path('administrations/', include('administrations.urls')),
]
