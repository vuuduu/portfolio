from django.shortcuts import render
from blog.models import Post, Comment
from blog.forms import CommentForm

# Create your views here.
# blog_index will display a list of all your posts
def blog_index(request):
    # get all post but order them by when they were created
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)

# blog_category similar to blog_index, but posts viewed will only be of a specific category chosen by the user
def blog_category(request, category):
    # filter tell Django what conditions need to be met for an object to be retrieved
    posts = Post.objects.filter(categories__name__contains=category).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)

# blog_details display a full post as well as comments and a form to allow users to create new comments.
def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    # checking if a comment in the form send a Post request to create an instance of comment
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        # checking if all the field in the form has been entered correctly
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save() # record the time that the comment was posted

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog_detail.html", context)
