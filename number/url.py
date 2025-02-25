from django.urls import path
from .views import *

urlpatterns = [
    path('numbers/', NumberListCreateAPIView.as_view()),
    path('numbers/<int:pk>/', NumberUpdateAPIView.as_view(), name='number-update'),  # ✅ Update endpoint
    path('numbers/<int:pk>/delete/', NumberDeleteAPIView.as_view(), name='number-delete'),  # ✅ Delete endpoint
]