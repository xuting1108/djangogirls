from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())\
        .order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
#o "render" vai renderizar o modelo de acordo com o template
# blog/post_list e retornara o resultado