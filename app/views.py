from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from app.models import BlogPost


def home(request):
    blogposts = BlogPost.objects.all()
    return render_to_response('home.html', {'blogposts':blogposts})