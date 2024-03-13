
from django.urls import path
from . import views
from knox.views import LogoutView, LogoutAllView



urlpatterns = [
    path('create-user/', views.CreateUser.as_view()),
    path('login/', views.LoginView.as_view(), name='knox_login'),
    path('logout/', LogoutView.as_view()),
    path('logout-all/', LogoutAllView.as_view()),
]
