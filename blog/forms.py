from .models import Comment, Post
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'featured_image',
        ]
        widgets = {
    'content': SummernoteWidget(),
    }