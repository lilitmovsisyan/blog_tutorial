from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    #we define a QuerySet, posts. This will be passed to the template rendered by tis view function.
    posts = Post.objects.filter(date_published__lte=timezone.now()).order_by('date_published')
    return render(request, 'blog/post_list.html', {'posts': posts})
    #the render function takes 3 arguments:
    #1. request = everything we receive from the user via the internet.
    #2. the template file.
    #3. {} = a place in which we can add things for the template to use. This is a dictionary. 
    #so pass the posts variable defined above into this dictionary with a key: {'posts': posts}