from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        input_class = 'w-full px-4 py-3 rounded-xl bg-surface border border-border text-text-primary placeholder-text-muted focus:outline-none focus:border-primary transition-colors'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = input_class
            field.widget.attrs.pop('autofocus', None)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data.get('first_name', '')
        user.last_name = self.cleaned_data.get('last_name', '')
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        input_class = 'w-full px-4 py-3 rounded-xl bg-surface border border-border text-text-primary placeholder-text-muted focus:outline-none focus:border-primary transition-colors'
        for field in self.fields.values():
            field.widget.attrs['class'] = input_class


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'location', 'website', 'github', 'twitter', 'linkedin', 'skills']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
            'avatar': forms.FileInput(attrs={'class': 'hidden', 'id': 'avatar-input', 'accept': 'image/*'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        input_class = 'w-full px-4 py-3 rounded-xl bg-surface border border-border text-text-primary placeholder-text-muted focus:outline-none focus:border-primary transition-colors'
        for name, field in self.fields.items():
            if name != 'avatar':
                field.widget.attrs['class'] = input_class
