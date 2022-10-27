from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
# Create your views here.
class BlogListView(ListView):
    template_name = 'home.html'
    model = Post

class BlogDetailView(DetailView):
    template_name = "post_detail.html"
    model = Post