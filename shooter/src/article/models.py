from django.db import models

from userprofile.models import User

class Article(models.Model):
	id = models.AutoField(db_column='ArticleID', primary_key=True)
	title = models.CharField(db_column='Title', max_length=200)
	body = models.TextField(db_column='Content')
	pub_date = models.DateTimeField('date published',db_column='PublishedDate', auto_now_add=True)
	likes = models.IntegerField(default=0, db_column='Likes')
	userid = models.ForeignKey(User, db_column='UserID')

	class Meta:
		db_table = 'Article'
		ordering = ['-pub_date']

	def __str__(self):
		return self.title


class Comment(models.Model):
	id = models.AutoField(db_column='CommentID', primary_key=True)
	first_name = models.CharField(max_length=200, db_column='Name')
	body = models.TextField(db_column='Content')
	pub_date = models.DateTimeField('date published', db_column='PublishedDate', auto_now_add=True)
	article = models.ForeignKey(Article, db_column='ArticleID')

	class Meta:
		db_table = 'Comment'

	def __str__(self):
		return str(self.first_name + " | " + self.article.title)
