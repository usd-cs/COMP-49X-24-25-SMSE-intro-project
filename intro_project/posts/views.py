"""
Views File.
"""
#from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from posts.models import Post

@csrf_exempt #bypasses Django's CSRF protection (TODO: look into this more)
@login_required
def create_post(request):
    """
    Handles creating new posts and allows only logged in users to create a new post.
    Args: request (HttpRequest): The Http request
    Returns: JsonResponse: The JSON response shows either success or failure
    """
    if request.method == "POST":
        # parse JSON data
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()

        if not title or not content:
            return JsonResponse({"error": "Title and content are required."}, status=400) #400 Bad Request (Client error response)

        post = Post.objects.create(
            title=title,
            content=content,
            author=request.user
        )
        return JsonResponse({"message": "You're logged in! Post created successfully.", "post_id": post.id}, status=201) #Created (Successful)

    return JsonResponse({"error": "Invalid request method."}, status=405) # 405 Method not Allowed
