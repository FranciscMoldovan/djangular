from django.conf.urls import url
from .api import LoginView, LogoutView
from django.urls import include, path

urlpatterns = [
    path(r'login/', LoginView.as_view()),
    path(r'logout/', LogoutView.as_view())
]