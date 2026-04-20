from blog.models import Category


from django.db.models import Count, Q

def global_context(request):
    categories = Category.objects.annotate(
        num_posts=Count('posts', filter=Q(posts__status='published'))
    ).order_by('-num_posts')[:8]
    return {
        'global_categories': categories,
    }
