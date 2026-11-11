from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import PostViewSet, GroupViewSet, CommentViewSet


# Именованный роутер для порядка
router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet, basename='post')
router_v1.register('groups', GroupViewSet, basename='group')

v1_patterns = [
    path('api-token-auth/', obtain_auth_token),
    path('', include(router_v1.urls)),

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

# Связь префикс v1 со списком маршрутов
urlpatterns = [
    path('v1/', include(v1_patterns)),

    # Сюда в будущем можно добавить новый маршрут или версию апишки:
    # path('v2/', include(v2_patterns)),
]