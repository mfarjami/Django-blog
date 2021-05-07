from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
# Create your views here.

def LikeView(request, pk):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	post.likes.add(request.user)
	return HttpResponseRedirect(reverse('blog:detail', args=[str(pk)]))

class PostList(ListView):
	model = Post
	ordering = ['-publish']

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(PostList, self).get_context_data(*args, **kwargs)
		context["cat_menu"]= cat_menu
		return context

def CategoryListView(request):
	cat_menu_list = Category.objects.all()
	return render(request, 'blog/category_list.html',{'cat_menu_list':cat_menu_list})

def CategoryView(request, cats):
	category_post = Post.objects.filter(category=cats)
	return render(request, 'blog/categories.html',{'cats':cats.title(), 'category_post':category_post})

class PostDetail(DetailView):
	model = Post

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(PostDetail, self).get_context_data(*args, **kwargs)
		stuff = get_object_or_404(Post, id=self.kwargs['pk'])
		total_likes = stuff.total_likes()
		context["cat_menu"]= cat_menu
		context["total_likes"] = total_likes
		return context



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
