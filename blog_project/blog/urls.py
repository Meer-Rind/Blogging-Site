from django.urls import path
from .views import CustomLoginView, CustomLogoutView, ProfileView  # Add this import

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    register,
    add_comment,
    like_post,
    about,
)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),  # Add this line
    path('register/', register, name='register'),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comment/', add_comment, name='add-comment'),
    path('post/<int:pk>/like/', like_post, name='like-post'),
    path('about/', about, name='about'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]