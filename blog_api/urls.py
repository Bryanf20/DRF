from django.urls import path
from .views import PostList, PostDetail, PostListDetailfilter, CreatePost, EditPost, DeletePost, AdminPostDetail
# from rest_framework.routers import DefaultRouter

app_name = 'blog_api'

urlpatterns = [
    path('', PostList.as_view(), name='listcreate'),
    path('posts/<slug:slug>/', PostDetail.as_view(), name='post-detail'),
    path('search/', PostListDetailfilter.as_view(), name='postsearch'),
    # Post Admin URLs
    path('admin/create/', CreatePost.as_view(), name='createpost'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('admin/edit/postdetail/<int:pk>/', AdminPostDetail.as_view(), name='adminpostdetail'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),
]

# router = DefaultRouter()
# router.register('', PostList, basename='post')

# urlpatterns = router.urls
