from django import forms
from .models import Post, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'excerpt', 'category', 'tags', 'status', 'featured', 'cover_image', 'read_time']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-xl bg-surface border border-border text-text-primary placeholder-text-muted focus:outline-none focus:border-primary transition-colors',
                'placeholder': 'Enter your post title...',
            }),
            'content': forms.Textarea(attrs={
                'id': 'content-editor',
                'class': 'w-full h-96 px-4 py-3 rounded-xl bg-surface border border-border text-text-primary font-mono text-sm focus:outline-none focus:border-primary transition-colors',
                'placeholder': '# Write your post in Markdown\n\nSupports **bold**, *italic*, `code`, and code blocks...',
            }),
            'excerpt': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 rounded-xl bg-surface border border-border text-text-primary placeholder-text-muted focus:outline-none focus:border-primary transition-colors',
                'placeholder': 'Short description of your post (optional)...',
                'rows': 3,
            }),
            'category': forms.Select(attrs={
                'class': 'w-full px-4 py-3 rounded-xl bg-surface border border-border text-text-primary focus:outline-none focus:border-primary transition-colors',
            }),
            'tags': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-xl bg-surface border border-border text-text-primary placeholder-text-muted focus:outline-none focus:border-primary transition-colors',
                'placeholder': 'python, django, web-dev (comma separated)',
                'data-role': 'tagsinput',
            }),
            'status': forms.Select(attrs={
                'class': 'w-full px-4 py-3 rounded-xl bg-surface border border-border text-text-primary focus:outline-none focus:border-primary transition-colors',
            }),
            'read_time': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 rounded-xl bg-surface border border-border text-text-primary focus:outline-none focus:border-primary transition-colors',
                'min': 1,
            }),
            'featured': forms.CheckboxInput(attrs={
                'class': 'w-5 h-5 text-primary rounded',
            }),
            'cover_image': forms.FileInput(attrs={
                'class': 'hidden',
                'id': 'cover-image-input',
                'accept': 'image/*',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'].help_text = 'Add tags separated by commas'
        self.fields['cover_image'].required = False
        self.fields['category'].empty_label = "Select Category"
