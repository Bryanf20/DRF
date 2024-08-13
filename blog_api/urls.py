from django.urls import path
from .views import PostList, PostDetail, PostListDetailfilter
# from rest_framework.routers import DefaultRouter

app_name = 'blog_api'

urlpatterns = [
    # path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    # path('posts/<str:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('posts/<slug:slug>/', PostDetail.as_view(), name='post-detail'),
    # path('posts/', PostDetail.as_view(), name='detailcreate'),
    # path('search/', PostSearch.as_view(), name='postsearch')
    path('search/', PostListDetailfilter.as_view(), name='postsearch'),
    path('', PostList.as_view(), name='listcreate')
]

# router = DefaultRouter()
# router.register('', PostList, basename='post')

# urlpatterns = router.urls
