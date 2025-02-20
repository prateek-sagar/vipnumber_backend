from django.urls import path
from .views import *

urlpatterns = [
    path('numbers/', NumberListCreateAPIView.as_view())
]