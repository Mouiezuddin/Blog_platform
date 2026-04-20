from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 rounded-xl bg-surface border border-border text-text-primary placeholder-text-muted focus:outline-none focus:border-primary transition-colors resize-none',
                'rows': 4,
                'placeholder': 'Share your thoughts...',
            }),
        }
