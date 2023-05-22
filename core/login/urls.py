from django.urls import path

from core.login.views import *

urlpatterns = [
    path('', LoginAuthView.as_view(), name='login'),
    path('different/', LoginAuthView.as_view(), name='login_different'),
    path('reset/password/', LoginResetPasswordView.as_view(), name='login_reset_password'),
    path('logout/', LoginLogoutRedirectView.as_view(), name='login_logout'),
    path('update/password/<str:pk>/', LoginUpdatePasswordView.as_view(), name='login_update_password'),
]
