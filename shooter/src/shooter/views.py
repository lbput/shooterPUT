from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.db.models import Count
from django.utils import timezone

from article.models import Article


def home(request):
	return render_to_response('index.html',
	 			{'articles' : Article.objects.annotate(comment_count=Count('comment')).all()[:3],
				'today' : timezone.localtime(timezone.now()) },
				context_instance=RequestContext(request))

def aboutus(request):
	return render_to_response("aboutus.html", locals(), context_instance=RequestContext(request))

