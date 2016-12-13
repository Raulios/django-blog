from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}

    return render(request, 'blog_frontend/index.html', context)