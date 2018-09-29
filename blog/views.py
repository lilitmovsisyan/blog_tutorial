from django.shortcuts import render, get_object_or_404
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

def post_detail(request, pk):
    #post = Post.objects.get(pk=pk) 
    # #-------------^ this version will return an ugly DoesNotExist error if we try to GET a page for which there is no post,
    #e.g. if we try to GET the post with pk=10, but there are only 4 blog posts. SO instead we tell django to return
    #a much nicer 404 error if there is no such pk:
    
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
