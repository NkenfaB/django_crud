from django import forms
from .models import Post

class Post(forms):
    class Meta:
        model =  Post
        fields = [
            "title",
            "slug",
            "author",
            "body",
            "published",
            "created",
            "updated",
            "status" 
        ]