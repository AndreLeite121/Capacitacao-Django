from django.shortcuts import render

from .models import Post

# Create your views here.


def index(request):

    postagem = Post.objects.all()

    context={
        'post' : postagem
    }

    return render(request, 'index.html', context)