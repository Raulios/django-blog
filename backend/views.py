from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from core.models import Post

# Create your views here.
@login_required()
def index(request):
    context = {}
    context['nav_active'] = 'index'

    print 'hey'
    return render(request, 'backend/index.html', context)

@login_required()
def posts(request):
    context = {}
    context['nav_active'] = 'posts'

    post_list = Post.objects.all()

    paginator = Paginator(list(reversed(post_list)), 10)

    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context['posts'] = posts

    return render(request, 'backend/posts.html', context)

@login_required()
def edit_post(request, post_id):
    context = {}
    context['nav_active'] = 'posts'

    post = Post.objects.get(pk=post_id)

    context['post'] = post

    return render(request, 'backend/index.html', context)