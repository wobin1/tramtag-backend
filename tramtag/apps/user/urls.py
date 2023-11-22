from django.urls import path
from .views import TramtagUser, SingleUser


urlpatterns = [
    path('users/', TramtagUser.as_view()),
    path('user/<str:id>', SingleUser.as_view())
]