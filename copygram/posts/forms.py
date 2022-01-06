"""Post forms."""

#django
from django import forms
#models
from posts.models import Post

class PostForm(forms.ModelForm):
    """Post Model form."""
    class Meta:
        """Form Settings"""
        model= Post
        fields= ('profile', 'title', 'photo')