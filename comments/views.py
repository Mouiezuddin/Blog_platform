from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from blog.models import Post
from .models import Comment
from .forms import CommentForm


@login_required
@require_POST
def add_comment(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug, status='published')
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.author = request.user
        parent_id = request.POST.get('parent_id')
        if parent_id:
            try:
                parent = Comment.objects.get(id=parent_id, post=post)
                comment.parent = parent
            except Comment.DoesNotExist:
                pass
        comment.save()
        messages.success(request, 'Comment posted successfully!')
    else:
        messages.error(request, 'Error posting comment.')
    return redirect('blog:post_detail', slug=post_slug)


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment updated!')
            return redirect('blog:post_detail', slug=comment.post.slug)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'comments/edit_comment.html', {'form': form, 'comment': comment})


@login_required
@require_POST
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    post_slug = comment.post.slug
    comment.delete()
    messages.success(request, 'Comment deleted.')
    return redirect('blog:post_detail', slug=post_slug)
