from rest_framework import serializers
from .models import Board, Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source= 'user.nickname')
    created_at = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta: 
        model = Comment
        fields = ['id', 'post', 'user', 'created_at', 'comment']
        read_only_fields = ['user', 'post', 'created_at']


class BoardSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta: 
        model = Board
        fields = ['id', 'user', 'title', 'body', 'comments']
        read_only_fields = ['user']


