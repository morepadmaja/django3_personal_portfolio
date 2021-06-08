from django.shortcuts import render, get_object_or_404
from .models import Project_class

def all_blogs(request):
    blogs=Project_class.objects.all()
    return render(request, 'blog/all_blogs.html',{'blogs':blogs})

def details(request,blog_id):
    blog = get_object_or_404(Project_class, pk=blog_id)
    return render(request,'blog/details.html',{'blog': blog})
