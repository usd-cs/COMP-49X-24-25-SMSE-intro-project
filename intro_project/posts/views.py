"""
Views File for handling post features in the post app.
"""
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from posts.models import Post


def index(request):
    #show all posts from the database
    posts = Post.objects.all()
    output = "\n".join([f"{post.title}: {post.content} : {post.author} : {post.created_at}" for post in posts])
    return HttpResponse(output, content_type="text/plain")

@csrf_exempt #bypasses Django's CSRF protection (TODO: look into this more)
@login_required

def create_post(request):
    """
    Handles creating new posts and allows only logged in users to create a new post.
    Args: request (HttpRequest): The Http request
    Returns: JsonResponse: The JSON response shows either success or failure
    """
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Login is required."}, status=302) #redirects to login page by default

    if request.method == "POST":
        # parse JSON data
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()

        #check that data is valid
        if not title or not content:
            return JsonResponse({"error": "data needs to title  and content"}, status=400) #400 Bad Request (Client error response)

        #creates the post
        post = Post.objects.create(
            title=title,
            content=content,
            author=request.user
        )
        return JsonResponse({"message": "You're logged in! Post created successfully.", "post_id": post.id}, status=201) #Created (Successful)

    return JsonResponse({"error": "Invalid request method."}, status=405) # 405 Method not Allowed

