from django.urls import path
from .views import UserAuthentication, TokenRefresh, ForgotPassword, ResetPassword, UserVerification


urlpatterns = [
    path('login/', UserAuthentication.as_view()),
    path('refresh_token/', TokenRefresh.as_view()),
    path('forgot-password/', ForgotPassword.as_view()),
    path('reset-password/<str:token>', ResetPassword.as_view()),
    path('verify-user/<str:token>', UserVerification.as_view())
]