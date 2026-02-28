from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Post, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    @action(detail=True, methods=['get'])
    def stats(self, request, pk=None):
        user = self.get_object()
        post_count = user.posts.count()
        comment_count = user.comments.count()
        
        return Response({
            'user_id': user.id,
            'username': user.username,
            'total_posts': post_count,
            'total_comments': comment_count
        })


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    @action(detail=False, methods=['get'])
    def lightweight(self, request):
        posts = self.get_queryset().values('id', 'title', 'created_at')
        return Response(posts)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer