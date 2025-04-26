from rest_framework import serializers, viewsets, permissions
from .models import BlogPost, Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'author', 'text', 'created_date']

class BlogPostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()
    
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author', 'date_posted', 'image', 'likes_count', 'comments']
    
    def get_likes_count(self, obj):
        return obj.likes.count()

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all().order_by('-date_posted')
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        post_id = self.request.data.get('post')
        post = BlogPost.objects.get(pk=post_id)
        serializer.save(author=self.request.user, post=post)