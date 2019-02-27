from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})
#o "render" vai renderizar o modelo de acordo com o template
# blog/post_list e retornara o resultado