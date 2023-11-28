from django.urls import path
from .views import FounderView, SingleFounderView


urlpatterns = [
    path('founder/', FounderView.as_view()),
    path('founder/<str:id>', SingleFounderView.as_view()),
]