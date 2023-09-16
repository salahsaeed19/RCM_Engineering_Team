from django import forms
from .models import Post, Comment, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'content', 'bio', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']