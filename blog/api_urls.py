from django.urls import path
from . import api_views

app_name = 'api'

urlpatterns = [
    path('posts/', api_views.PostListAPIView.as_view(), name='post-list'),
    path('posts/<slug:slug>/', api_views.PostDetailAPIView.as_view(), name='post-detail'),
    path('categories/', api_views.CategoryListAPIView.as_view(), name='category-list'),
]
