from django.urls import path
from .views.user.views import *

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('add/', UserCreateView.as_view(), name='user_create'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
    path('update/profile/', UserUpdateProfileView.as_view(), name='user_update_profile'),
    path('update/password/', UserUpdatePasswordView.as_view(), name='user_update_password'),
    path('choose/profile/<int:pk>/', UserChooseProfileView.as_view(), name='user_choose_profile'),
]
