from django.urls import include, path
from rest_framework import routers
# from rest_framework.routers import DefaultRouter

# from .views import CustomUserViewSet
from .views import FollowViewSet


app_name = 'api'
router = routers.DefaultRouter()
# router.register('users', FollowViewSet)

router.register(r'subscriptions', FollowViewSet, basename='subscriptions')
router.register(
    r'(?P<title_id>\d+)/subscriptions', FollowViewSet, basename='subscriptions')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
