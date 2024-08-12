from django.urls import path
from .views import CommentViewSet

urlpatterns = [
    path('comments/', CommentViewSet.as_view(), name='comment'),
]
