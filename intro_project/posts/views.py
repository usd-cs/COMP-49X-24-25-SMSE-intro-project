"""
Views File for handling post features in the post app.
"""
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views import generic
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Post, Comment

def home(request):
    """
    Displays the home page with all the posts and comments. If a useris logged in, they can add posts and comments.
    """
    posts = Post.objects.all()
    #output = "\n".join([f"{post.title}: {post.content} : {post.author} : {post.created_at}" for post in posts])
    print(posts)
    return render (request, "posts/home.html", {"posts": posts})
    #return HttpResponse(output, content_type="text/plain")

@login_required
def create_post(request):
    """
    Handles creating new posts and allows only logged in users to create a new post.
    Args: request (HttpRequest): The Http request
    Returns: JsonResponse: The JSON response shows either success or failure
    """
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Login is required."}, status=302) #redirects to login page by default

    if request.method == 'POST':
        content = request.POST.get('content', '').strip()
        if not content:
            return JsonResponse({
                "error": "Content cannot be empty"
            }, status=400)

        Post.objects.create(
            content=content,
            author=request.user
        )
    return redirect('posts:home')

@login_required
def create_comment(request, post_id):
    """
    Handles creating new comments and allows only logged in users to create a new comment.
    """
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        Comment.objects.create(
            content=request.POST['content'],
            author=request.user,
            post=post
        )
    return redirect('posts:home')

@login_required
def delete_post(request, post_id):
    """
    Handles deleting a post and allows only superusers to delete a post.
    """
    if not request.user.is_authenticated or not request.user.is_superuser:
        return HttpResponseForbidden("You're not a superuser'.")

    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('posts:home')

@login_required
def delete_comment(request, comment_id):
    """
    Handles deleting a comment and allows only superusers to delete a comment.
    """
    if not request.user.is_authenticated or not request.user.is_superuser:
        return HttpResponseForbidden("You're not a superuser")
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('posts:home')

