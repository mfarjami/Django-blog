from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
# Create your views here.

class PostList(ListView):
	model = Post
	ordering = ['-publish']

class PostDetail(DetailView):
	model = Post


class PostCreate(CreateView):
	model = Post
	form_class = PostForm
	# fields = '__all__'

class PostUpdate(UpdateView):
	model = Post
	form_class = UpdateForm
	# fields = ('title','body')
	template_name = 'blog/post_update.html'

class PostDelete(DeleteView):
	model = Post
	success_url = reverse_lazy('blog:home')
