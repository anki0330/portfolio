from django.shortcuts import render,get_object_or_404
from .models import blogs

def myblog(request):
    Myblog = blogs.objects
    return render(request,'myblogs/myblogs.html',{"Myblog":Myblog})

def detail(request,blog_id):
   detailblog = get_object_or_404(blogs,pk=blog_id)
   return render(request,'myblogs/detail.html',{"detailblog":detailblog})

