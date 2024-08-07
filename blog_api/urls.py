# from django.urls import path
from .views import PostList
from rest_framework.routers import DefaultRouter

app_name = 'blog_api'

# urlpatterns = [
#     path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
#     path('', PostList.as_view(), name='listcreate')
# ]

router = DefaultRouter()
router.register('', PostList, basename='post')

urlpatterns = router.urls
