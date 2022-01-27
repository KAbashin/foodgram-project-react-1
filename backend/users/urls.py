from django.urls import include, path
from rest_framework import routers

from .views import FollowViewSet


router = routers.DefaultRouter()

router.register(r'subscriptions', FollowViewSet, basename='subscriptions')
router.register(
    r'(?P<title_id>\d+)/subscriptions', FollowViewSet, basename='subscriptions')

urlpatterns = [
    path('', include(router.urls)),
]