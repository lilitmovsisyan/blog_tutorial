from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

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


def post_new(request):

    if method == "POST":
        #if the method is POST, we want to construct an instance of PostForm 
        #using the data entered by the user, which is stored in request.POST:
        form = PostForm(request.POST)
        
        #Next, we must use the method is_valid() on this object we have constructed
        #to check the form input is correct:
        if form.is_valid():
            post = form.save(commit=False) #commit=False means we aren't yet finished (not ready to preserve changes)
            post.author = request.user
            post.date_published =  timezone.now
            post.save() #this will preserve changes i.e. create the new instance of a complete post. 

            #now we want to redirect to the post_detail page to view our post, 
            #so pass the post_detail view and the pk for this post into the redirect() function:
            return redirect('post_detail', pk=post.pk) 
            #NB: redirect() takes the value of the view function and anythin to be pass to it,
            #whereas render() (see below) takes the urlpattern - i.e. a HTTPrequest, url path, and any input model.

    else:
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})