from django.shortcuts import render
from django.contrib.auth.models import User


from rest_framework import viewsets


from .models import Comment, Feed
from .serializers import CommentSerializer, FeedSerializer, UserSerializer


# Create your views here.
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

