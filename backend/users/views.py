from .models import Follow
from .serializers import FollowSerializers
from rest_framework import viewsets


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializers
