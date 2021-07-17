from django.db import models

# Create your models here.

class user(models.Model):
	user_name = models.CharField(max_length=250)
	password = models.CharField(max_length=16)


class user_posts(models.Model):
	userId = models.IntegerField()
	postId = models.IntegerField()
	title = models.CharField(max_length=2000)
	body = models.TextField()