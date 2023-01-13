from django.urls import path

from .views import (Registration, Authorization, Logout, NewTokenPair, ConfirmEmail, ForgotPassword,
                    ForgotPasswordConfirm, CheckTokenView)

urlpatterns = [
    path("auth/register/", Registration.as_view()),
    path("auth/authorize/", Authorization.as_view()),
    path("auth/logout/", Logout.as_view()),
    path("auth/token_pair/", NewTokenPair.as_view()),
    path("auth/confirm_email/", ConfirmEmail.as_view()),
    path("auth/forgot_password/", ForgotPassword.as_view()),
    path("auth/confirm_password/", ForgotPasswordConfirm.as_view()),
    path("auth/check_token/", CheckTokenView.as_view())
]