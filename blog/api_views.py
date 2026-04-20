from rest_framework import generics
from django.db.models import Q
from .models import Post, Category
from .serializers import PostListSerializer, PostDetailSerializer, CategorySerializer


class PostListAPIView(generics.ListAPIView):
    serializer_class = PostListSerializer

    def get_queryset(self):
        queryset = Post.objects.filter(status='published').select_related('author', 'category').prefetch_related('tags')
        q = self.request.query_params.get('q')
        category = self.request.query_params.get('category')
        tag = self.request.query_params.get('tag')
        if q:
            queryset = queryset.filter(Q(title__icontains=q) | Q(content__icontains=q))
        if category:
            queryset = queryset.filter(category__slug=category)
        if tag:
            queryset = queryset.filter(tags__slug=tag)
        return queryset


class PostDetailAPIView(generics.RetrieveAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.filter(status='published')
    lookup_field = 'slug'


class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
