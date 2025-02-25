from django.urls import path
from .views import *

urlpatterns = [
    path("register/", register_user),
    path('login/', login_user),
    path('delete/', delete_user),
    path('update/', update_user)
]