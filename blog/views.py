from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Posts

# Create your views here.



class ListPostView(ListView):
    model = Posts
    template_name = 'list_posts.html'

class DetailedPostView(DetailView):
    model = Posts
    template_name = 'deatiled_post.html'

