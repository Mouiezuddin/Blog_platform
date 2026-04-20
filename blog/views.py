from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Count
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Post, Category, Like, Bookmark
from comments.models import Comment
from .forms import PostForm


def home(request):
    featured_posts = Post.objects.filter(status='published', featured=True).select_related('author', 'author__profile', 'category')[:3]
    recent_posts = Post.objects.filter(status='published').select_related('author', 'author__profile', 'category').prefetch_related('tags')[:9]
    categories = Category.objects.annotate(num_posts=Count('posts', filter=Q(posts__status='published'))).order_by('-num_posts')[:8]
    popular_posts = Post.objects.filter(status='published').order_by('-views')[:5]
    
    context = {
        'featured_posts': featured_posts,
        'recent_posts': recent_posts,
        'categories': categories,
        'popular_posts': popular_posts,
    }
    return render(request, 'blog/home.html', context)


def post_list(request):
    posts = Post.objects.filter(status='published').select_related('author', 'author__profile', 'category').prefetch_related('tags')
    
    # Search
    query = request.GET.get('q', '')
    category_slug = request.GET.get('category', '')
    tag_slug = request.GET.get('tag', '')
    
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    
    if category_slug:
        posts = posts.filter(category__slug=category_slug)
    
    if tag_slug:
        posts = posts.filter(tags__slug=tag_slug)
    
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = Category.objects.annotate(num_posts=Count('posts', filter=Q(posts__status='published'))).order_by('-num_posts')
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'query': query,
        'category_slug': category_slug,
        'tag_slug': tag_slug,
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    post.increment_views()
    
    comments = post.comments.filter(is_approved=True, parent=None).select_related('author', 'author__profile').prefetch_related('replies__author', 'replies__author__profile')
    
    related_posts = Post.objects.filter(
        status='published',
        category=post.category
    ).exclude(pk=post.pk).select_related('author', 'author__profile')[:3]
    
    is_liked = False
    is_bookmarked = False
    if request.user.is_authenticated:
        is_liked = Like.objects.filter(user=request.user, post=post).exists()
        is_bookmarked = Bookmark.objects.filter(user=request.user, post=post).exists()
    
    context = {
        'post': post,
        'comments': comments,
        'related_posts': related_posts,
        'is_liked': is_liked,
        'is_bookmarked': is_bookmarked,
        'content_html': post.get_content_as_html(),
    }
    return render(request, 'blog/post_detail.html', context)


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if post.status == 'published':
                post.published_at = timezone.now()
            post.save()
            form.save_m2m()
            messages.success(request, 'Post created successfully!')
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = PostForm()
    
    return render(request, 'blog/post_form.html', {'form': form, 'action': 'Create'})


@login_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            if post.status == 'published' and not post.published_at:
                post.published_at = timezone.now()
            post.save()
            form.save_m2m()
            messages.success(request, 'Post updated successfully!')
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'blog/post_form.html', {'form': form, 'post': post, 'action': 'Edit'})


@login_required
def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('blog:dashboard')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})


@login_required
def dashboard(request):
    posts = Post.objects.filter(author=request.user).select_related('category').prefetch_related('tags').order_by('-created_at')
    
    total_views = sum(p.views for p in posts)
    total_likes = sum(p.like_count for p in posts)
    total_comments = sum(p.comment_count for p in posts)
    published_count = posts.filter(status='published').count()
    draft_count = posts.filter(status='draft').count()
    
    context = {
        'posts': posts,
        'total_views': total_views,
        'total_likes': total_likes,
        'total_comments': total_comments,
        'published_count': published_count,
        'draft_count': draft_count,
    }
    return render(request, 'blog/dashboard.html', context)


def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(status='published', category=category).select_related('author', 'author__profile').prefetch_related('tags')
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'category': category,
        'page_obj': page_obj,
    }
    return render(request, 'blog/category_posts.html', context)


@login_required
@require_POST
def toggle_like(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
        liked = False
    else:
        liked = True
    return JsonResponse({'liked': liked, 'like_count': post.like_count})


@login_required
@require_POST
def toggle_bookmark(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    bookmark, created = Bookmark.objects.get_or_create(user=request.user, post=post)
    if not created:
        bookmark.delete()
        bookmarked = False
    else:
        bookmarked = True
    return JsonResponse({'bookmarked': bookmarked})


@login_required
def bookmarks(request):
    bookmarked_posts = Post.objects.filter(bookmarks__user=request.user, status='published').select_related('author', 'author__profile', 'category').prefetch_related('tags')
    paginator = Paginator(bookmarked_posts, 9)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'blog/bookmarks.html', {'page_obj': page_obj})


def search(request):
    query = request.GET.get('q', '').strip()
    posts = []
    if query:
        posts = Post.objects.filter(
            status='published'
        ).filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query) |
            Q(category__name__icontains=query)
        ).distinct().select_related('author', 'author__profile', 'category')
    
    paginator = Paginator(posts, 9)
    page_obj = paginator.get_page(request.GET.get('page'))
    
    return render(request, 'blog/search.html', {'page_obj': page_obj, 'query': query})
