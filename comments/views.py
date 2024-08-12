import logging
from rest_framework import generics, mixins, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Comment
from .serializers import CommentSerializer

logger = logging.getLogger(__name__)

class CommentPagination(PageNumberPagination):
    page_size = 25

class CommentViewSet(generics.GenericAPIView,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin):
    queryset = Comment.objects.prefetch_related('replies')
    serializer_class = CommentSerializer
    parser_classes = (MultiPartParser,)
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    pagination_class = CommentPagination

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        logger.info("Authorization Header: %s", request.headers.get('Authorization'))
        return self.create(request, *args, **kwargs)
