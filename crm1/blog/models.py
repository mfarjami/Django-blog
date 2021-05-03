from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import datetime
# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	body = models.TextField()
	publish = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def get_absolute_url(self):
		# return reverse('blog:detail', args=(str(self.id)))
		return reverse('blog:home')