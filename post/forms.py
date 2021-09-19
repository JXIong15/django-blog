from django import forms
from .models import Post

# CRUD - Create
class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'created_at')

#CRUD - Update
class PostUpdateForm(forms.ModelForm):
    #form for updating Posts
    class Meta:
        model = Post
        fields = ('title', 'body', 'created_at')
