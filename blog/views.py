from django.shortcuts import render
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView
)
# from django.urls import reverse_lazy
from .models import Post


def home(request):
	posts = Post.objects.all()
	return render(request, 'blog/home.html', locals())


class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']


class PostDetailView(DetailView):
	model = Post
	

class PostCreateView(CreateView):
	model = Post
	fields = ['title', 'content']
	# success_url = reverse_lazy('blog-home') 
	# If we want user get back on homepage after new post created

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	
	


def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})
