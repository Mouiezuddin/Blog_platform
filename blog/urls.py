from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.post_list, name='post_list'),
    path('search/', views.search, name='search'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('bookmarks/', views.bookmarks, name='bookmarks'),
    path('create/', views.post_create, name='post_create'),
    path('category/<slug:slug>/', views.category_posts, name='category_posts'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('<slug:slug>/delete/', views.post_delete, name='post_delete'),
    path('<slug:slug>/like/', views.toggle_like, name='toggle_like'),
    path('<slug:slug>/bookmark/', views.toggle_bookmark, name='toggle_bookmark'),
]
