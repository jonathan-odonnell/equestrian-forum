from rest_framework import serializers
from .models import Category, Comment, Post, Image


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'description', 'category', 'date', 'slug']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['post', 'image']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'comment', 'date', 'up_vote', 'down_vote']
