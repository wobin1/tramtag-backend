from django.urls import path
from .views import Startup


urlpatterns = [
    path('startup/', Startup.as_view())
]