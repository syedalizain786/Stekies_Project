from django.contrib import admin
from django.urls import include, path

from properties.views import PropertiesView

urlpatterns = [
    path('', PropertiesView.as_view())
]
