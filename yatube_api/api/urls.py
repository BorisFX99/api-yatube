from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('groups', GroupViewSet, basename='group')

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('', include(router.urls)),

    # Вложенные URL для комментариев
    path(
        'posts/<int:post_id>/comments/',
        CommentViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='comment-list',
    ),
    path(
        'posts/<int:post_id>/comments/<int:pk>/',
        CommentViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy',
        }),
        name='comment-detail',
    ),

]