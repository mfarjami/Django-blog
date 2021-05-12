from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
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

class Profile(models.Model):
	user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
	bio = models.TextField()
	profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
	facebook_url = models.CharField(max_length=255, null=True, blank=True)
	twitter_url = models.CharField(max_length=255, null=True, blank=True)
	instagram_url = models.CharField(max_length=255, null=True, blank=True)
	telegram_url = models.CharField(max_length=255, null=True, blank=True)

	def __str__(self):
		return str(self.user)

	def get_absolute_url(self):
		return reverse('blog:home')

class Post(models.Model):
	title = models.CharField(max_length=255)
	thumbanil = models.ImageField(null=True, blank=True, upload_to="images/")
	author = models.ForeignKey(User, on_delete=models.CASCADE)
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


class Comment(models.Model):
	post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	body = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s - %s' % (self.post.title , self.name)