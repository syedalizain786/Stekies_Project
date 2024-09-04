from django.contrib import admin
from django.urls import include, path

from properties.views import PropertiesView
from user.views import LoginView, User_Create_View, User_Updation_View, User_View


urlpatterns = [
    path('', User_View.as_view()),
    path('signup/', User_Create_View.as_view()),
    path('<int:id>/', User_View.as_view()),
    path('login/', LoginView.as_view()),
    path('update/<int:id>/', User_Updation_View.as_view()),
]
