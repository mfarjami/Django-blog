from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('blog:home')

class Post(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	body = RichTextField(blank=True, null=True)
	# body = models.TextField()
	publish = models.DateTimeField(auto_now_add=True)
	category = models.CharField(max_length=255, default='coding')
	snippet = models.CharField(max_length=255)
	likes = models.ManyToManyField(get_user_model(), related_name='blog_posts')

	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def get_absolute_url(self):
		# return reverse('blog:detail', args=(str(self.id)))
		return reverse('blog:home')