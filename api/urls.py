from properties.views import PropertiesView

from django.urls import path

urlpatterns = [
    path('properties/', PropertiesView.as_view()),
]
