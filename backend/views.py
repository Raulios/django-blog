from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from core.models import Post, Category, Tag
from backend.forms import PostForm, CategoryForm, TagForm

# Create your views here.
@login_required()
def index(request):
    context = {}
    context['nav_active'] = 'index'

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

@login_required()
def categories(request):
    context = {}
    context['nav_active'] = 'categories'

    categories_list = Category.objects.all()

    paginator = Paginator(list(reversed(categories_list)), 10)

    page = request.GET.get('page')

    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)

    context['categories'] = categories
    return render(request, 'backend/categories.html', context)

@login_required()
def add_category(request):
    context = {}
    context['nav_active'] = 'categories'

    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Category created.')

            return HttpResponseRedirect(reverse('user_panel_categories'))

    context['form'] = form

    return render(request, 'backend/edit_category.html', context)

@login_required()
def edit_category(request, category_id):
    context = {}
    context['nav_active'] = 'categories'

    category = Category.objects.get(pk=category_id)
    context['category'] = category

    form = CategoryForm(instance=category)

    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)

        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated.')

            return HttpResponseRedirect(reverse('user_panel_categories'))

    context['form'] = form

    return render(request, 'backend/edit_category.html', context)

@login_required()
def delete_category(request, category_id):
    context = {}
    context['nav_active'] = 'categories'

    category = Category.objects.get(pk=category_id)
    category.delete()

    messages.success(request, 'Category deleted.')

    return HttpResponseRedirect(reverse('user_panel_categories'))

@login_required()
def tags(request):
    context = {}
    context['nav_active'] = 'tags'

    tags_list = Tag.objects.all()

    paginator = Paginator(list(reversed(tags_list)), 10)

    page = request.GET.get('page')

    try:
        tags = paginator.page(page)
    except PageNotAnInteger:
        tags = paginator.page(1)
    except EmptyPage:
        tags = paginator.page(paginator.num_pages)

    context['tags'] = tags
    return render(request, 'backend/tags.html', context)

@login_required()
def add_tag(request):
    context = {}
    context['nav_active'] = 'tags'

    form = TagForm()

    if request.method == 'POST':
        form = TagForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Tag created.')

            return HttpResponseRedirect(reverse('user_panel_tags'))

    context['form'] = form

    return render(request, 'backend/edit_tag.html', context)

@login_required()
def edit_tag(request, tag_id):
    context = {}
    context['nav_active'] = 'tags'

    tag = Tag.objects.get(pk=tag_id)
    context['tag'] = tag

    form = TagForm(instance=tag)

    if request.method == 'POST':
        form = TagForm(request.POST, request.FILES, instance=tag)

        if form.is_valid():
            form.save()
            messages.success(request, 'Tag updated.')

            return HttpResponseRedirect(reverse('user_panel_tags'))

    context['form'] = form

    return render(request, 'backend/edit_tag.html', context)

@login_required()
def delete_tag(request, tag_id):
    context = {}
    context['nav_active'] = 'tags'

    tag = Tag.objects.get(pk=tag_id)
    tag.delete()

    messages.success(request, 'Tag deleted.')

    return HttpResponseRedirect(reverse('user_panel_tags'))