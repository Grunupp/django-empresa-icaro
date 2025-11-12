from django.shortcuts import render
from .models import Post

# Create your views here.
def posts(request):
    posts = Post.objects.order_by('-criado_em')
    context = {"posts":posts}
    return render(request,'posts.html',context)