from rest_framework import viewsets
from .models import Follow
from .serializers import FollowSerializers


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializers
