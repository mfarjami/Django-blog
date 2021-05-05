from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
# Create your views here.

class PostList(ListView):
	model = Post
	ordering = ['-publish']


def CategoryView(request, cats):
	category_post = Post.objects.filter(category=cats)
	return render(request, 'blog/categories.html',{'cats':cats.title(), 'category_post':category_post})

class PostDetail(DetailView):
	model = Post


class PostCreate(CreateView):
	model = Post
	form_class = PostForm
	# fields = '__all__'

class PostCategoryView(CreateView):
	model = Category
	# form_class = UpdateForm
	fields = '__all__'
	# template_name = 'blog/post_update.html'

class PostUpdate(UpdateView):
	model = Post
	form_class = UpdateForm
	# fields = ('title','body')
	template_name = 'blog/post_update.html'

class PostDelete(DeleteView):
	model = Post
	success_url = reverse_lazy('blog:home')
