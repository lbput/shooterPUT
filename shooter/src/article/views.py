from django.utils import timezone
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.template import RequestContext
from django.contrib import messages
from django.db.models import Count
from django.views.generic.base import TemplateView

from .models import Article, Comment
from .forms import CommentForm

from django.core.paginator import Paginator, InvalidPage, EmptyPage


def articles(request):
	news = Article.objects.annotate(comment_count=Count('comment')).all()
	paginator = Paginator(news, 4)
	
	try: page = int(request.GET.get("page", '1'))
	except ValueError: page = 1

	try:
		news = paginator.page(page)
	except (InvalidPage, EmptyPage):
		news = paginator.page(paginator.num_pages)

	return render_to_response('articles.html',
				{'articles' : news,
				'today' : timezone.localtime(timezone.now()) },
				context_instance=RequestContext(request))

def article(request, article_id=1):

	return render_to_response('article.html',
				{'article' : Article.objects.get(id=article_id),
				'form' : CommentForm()},
				context_instance=RequestContext(request) )


def like_article(request, article_id):
	if article_id:
		a = Article.objects.get(id=article_id)
		a.likes = a.likes + 1
		a.save()

	return HttpResponseRedirect('/articles/get/%s' % article_id)

def add_comment(request, article_id):
	a = Article.objects.get(id=article_id)

	if request.method == "POST":
		f = CommentForm(request.POST)
		if f.is_valid():
			c = f.save(commit=False)
			c.article = a
			c.save()
			#messages.success(request, "Dodano komentarz")
			return HttpResponseRedirect("/articles/get/%s" % article_id)
		else:
			return render_to_response('article.html', {'article' : a,'form':f},context_instance=RequestContext(request))
	
def delete_comment(request, comment_id):
	c = Comment.objects.get(id=comment_id)
	
	article_id = c.article.id
	c.delete()

	#messages.add_message(request, settings.DELETE_MESSAGE, "Usunięto komentarz.");

	return HttpResponseRedirect("/articles/get/%s" % article_id)
