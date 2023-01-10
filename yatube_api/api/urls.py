from django.urls import include, path

from rest_framework.authtoken import views
from rest_framework import routers

from api.views import GroupViewSet, PostViewSet, CommentViewSet


router_v1 = routers.DefaultRouter()
# не понял про поддержку версий из кода
router_v1.register('api/v1/posts', PostViewSet, basename='post')
router_v1.register('api/v1/groups', GroupViewSet, basename='group')
router_v1.register(
    r'api/v1/posts/(?P<id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)


urlpatterns = [
    path('', include(router_v1.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]
