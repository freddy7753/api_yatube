from django.urls import include, path

from rest_framework.authtoken import views
from rest_framework import routers

from api.views import GroupViewSet, PostViewSet, CommentViewSet


router = routers.DefaultRouter()
# не понял про поддержку версий из кода
router.register('posts', PostViewSet, basename='post')
router.register('groups', GroupViewSet, basename='group')
router.register(
    r'posts/(?P<id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)


urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]