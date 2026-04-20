from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'is_approved', 'get_is_reply', 'created_at']
    list_filter = ['is_approved', 'created_at']
    search_fields = ['author__username', 'content', 'post__title']
    list_editable = ['is_approved']
    actions = ['approve_comments']

    @admin.display(boolean=True, description='Reply?')
    def get_is_reply(self, obj):
        return obj.is_reply

    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)
    approve_comments.short_description = "Approve selected comments"
