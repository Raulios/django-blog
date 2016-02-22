from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from core.models import Post
from backend.forms import PostForm

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
def add_post(request):
    context = {}
    context['nav_active'] = 'posts'

    form = PostForm()

    if request.method == 'POST':
        print 'hey'
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Post created.')

            return HttpResponseRedirect(reverse('user_panel_posts'))

    context['form'] = form

    return render(request, 'backend/edit_post.html', context)

@login_required()
def edit_post(request, post_id):
    context = {}
    context['nav_active'] = 'posts'

    post = Post.objects.get(pk=post_id)
    context['post'] = post

    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated.')

            return HttpResponseRedirect(reverse('user_panel_posts'))

    context['form'] = form

    return render(request, 'backend/edit_post.html', context)

@login_required()
def delete_post(request, post_id):
    context = {}
    context['nav_active'] = 'posts'

    post = Post.objects.get(pk=post_id)
    post.delete()

    messages.success(request, 'Post deleted.')

    return HttpResponseRedirect(reverse('user_panel_posts'))