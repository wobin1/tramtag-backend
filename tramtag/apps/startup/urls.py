from django.urls import path
from .views import StartupView, SingleStartupView


urlpatterns = [
    path('startups/', StartupView.as_view()),
    path('startup/<str:id>', SingleStartupView.as_view())
]