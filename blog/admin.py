from django.contrib import admin
from .models import Post, Category, Like, Bookmark


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'get_post_count', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

    @admin.display(description='Posts')
    def get_post_count(self, obj):
        return obj.post_count


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'status', 'featured', 'views', 'get_like_count', 'get_comment_count', 'created_at']
    list_filter = ['status', 'featured', 'category', 'created_at']
    search_fields = ['title', 'content', 'author__username']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'created_at'
    list_editable = ['status', 'featured']
    readonly_fields = ['views', 'created_at', 'updated_at']

    @admin.display(description='Likes')
    def get_like_count(self, obj):
        return obj.like_count

    @admin.display(description='Comments')
    def get_comment_count(self, obj):
        return obj.comment_count
    fieldsets = (
        ('Content', {'fields': ('title', 'slug', 'author', 'content', 'excerpt', 'cover_image')}),
        ('Organization', {'fields': ('category', 'tags', 'status', 'featured')}),
        ('Metadata', {'fields': ('read_time', 'views', 'created_at', 'updated_at', 'published_at')}),
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'created_at']
    list_filter = ['created_at']


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'created_at']
