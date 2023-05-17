from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(DetailView):
    """ By default, DetailView will provide a context object we can use in our
    template called either object or the lowercased name of our model, which would be post. """
    
    #DetailView expects either a primary key or a slug passed to it as the identifier.

    model = Post
    template_name = "post_detail.html"
