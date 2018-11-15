from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


def home(request):
	posts = Post.objects.all()
	return render(request, 'blog/home.html', locals())


class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	# <app>/<model>_<viewtype>.html


def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})
