from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __set__(self):
		return self.title

	# reverse user to post-detail page after post creation
	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})