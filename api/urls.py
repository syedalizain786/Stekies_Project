from properties.views import PropertiesView

from django.urls import include, path

urlpatterns = [
    path('properties/', include('properties.urls')),
    path('user/',include('user.urls')),
]
