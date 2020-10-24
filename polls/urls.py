from django.urls import path
from . import views


urlpatterns = [
    path("register/", views.registerUser.as_view()),
    path("checkAuthentication/", views.checkAuthentication.as_view()),
    path("checkAuthentication2/", views.checkAuthentication2.as_view()),
    path("logout/", views.Logout.as_view()),
]
