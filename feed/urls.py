from django.urls import path, include


from rest_framework import routers, renderers
from rest_framework.urlpatterns import format_suffix_patterns 


from .views import CommentViewSet, FeedViewSet, UserViewSet

# router = routers.DefaultRouter()
# router.register(r'comments', CommentViewSet)
# router.register(r'feeds', FeedViewSet)
# router.register(r'users', UserViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

comment_list = CommentViewSet.as_view({
    'get':'list',
    'post': 'create'
}) 

comment_detail = CommentViewSet.as_view({
    'get':'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

feed_list = FeedViewSet.as_view({
    'get':'list',
    'post': 'create'
})


feed_detail = FeedViewSet.as_view({
    'get':'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = format_suffix_patterns([
    path('comments/', comment_list, name='comment-list'),
    path('comments/<int:pk>', comment_detail, name='comment-detail'),
    path('feeds/', feed_list, name='feed-list'),
    path('feeds/<int:pk>', feed_detail, name='feed-detail'),
])