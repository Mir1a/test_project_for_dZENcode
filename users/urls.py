from django.urls import path, include
from .views import UserViewSet

urlpatterns = [
    path('user/', UserViewSet.as_view(), name='user'),
]
