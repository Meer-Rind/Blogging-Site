from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import BlogPostViewSet, CommentViewSet  # Changed from ..api to .api

router = DefaultRouter()
router.register(r'posts', BlogPostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]