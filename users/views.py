from rest_framework import mixins, generics
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


class UserViewSet(generics.GenericAPIView,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,):
    queryset = User.objects.all().prefetch_related('comments')
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser,)
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        users = self.get_queryset()
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=201)
