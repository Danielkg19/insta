from django.contrib.auth.views import LoginView

from .views import *
from django.urls import path, include
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'save', SaveViewSet, basename='save')
router.register(r'saveitem', SaveItemViewSet, basename='saveitem')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('', include(router.urls)),
    path('user/', UserProfileListAPIView.as_view(), name='user_list'),
    path('user/<int:pk>', UserProfileDetailAPIView.as_view(), name='user_detail'),

    path('post/', PostListAPIView.as_view(), name='post_list'),
    path('post/<int:pk>', PostDetailAPIView.as_view(), name='post_detail'),
    path('post/create/', PostCreateAPIView.as_view(), name='post_create'),
    path('post_like/create/', PostCreateAPIView.as_view(), name='post_like_create'),
    path('post_comment/', PostCommentListAPIView.as_view(), name='post_comment_list'),
    path('post_comment/<int:pk>', PostCommentDetailAPIView.as_view(), name='post_comment_detail'),

    path('story/', StoryListAPIView.as_view(), name='story_list'),
    path('story/<int:pk>', StoryDetailAPIView.as_view(), name='story_detail'),
    path('story/create/', StoryCreateAPIView.as_view(), name='story_create'),

    path('comment/create/', CommentCreateAPIView.as_view(), name='comment_create'),
    path('comment_like/create', CommentLikeCreateAPIView.as_view(), name='comment_like_create'),
]