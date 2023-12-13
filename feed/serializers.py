from django.contrib.auth.models import User


from rest_framework import serializers


from .models import Comment, Feed


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','first_name', 'last_name', 'email']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'body', 'blog', 'comment', 'created_at']



class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ['id', 'user', 'content', 'active', 'created_at']
