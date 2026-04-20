from rest_framework import serializers
from django.contrib.auth.models import User
from taggit.serializers import TagListSerializerField, TaggitSerializer
from .models import Post, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'post_count']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class PostListSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    like_count = serializers.IntegerField(read_only=True)
    comment_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'author', 'excerpt', 'category', 'tags',
                  'status', 'featured', 'read_time', 'views', 'like_count',
                  'comment_count', 'created_at', 'published_at']


class PostDetailSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    like_count = serializers.IntegerField(read_only=True)
    comment_count = serializers.IntegerField(read_only=True)
    content_html = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'author', 'content', 'content_html',
                  'excerpt', 'category', 'tags', 'status', 'featured', 'read_time',
                  'views', 'like_count', 'comment_count', 'created_at', 'published_at']

    def get_content_html(self, obj):
        return obj.get_content_as_html()
