"""
Views File.
"""
#from django.shortcuts import render
from django.http import HttpResponse




def index(request):
<<<<<<< Updated upstream
=======
    #show all posts from the database
    posts = Post.objects.all()
    output = "\n".join([f"{post.title}: {post.content} : {post.author} : {post.created_at}" for post in posts])
    return HttpResponse(output, content_type="text/plain")

@csrf_exempt #bypasses Django's CSRF protection (TODO: look into this more)
@login_required
<<<<<<< Updated upstream

def create_post(request):
>>>>>>> Stashed changes
    """
    Handles getting an HHTP request and sends a HTTP response
    """
<<<<<<< Updated upstream
    return HttpResponse("Hello, world. You're at the posts index.")
=======
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

>>>>>>> Stashed changes
=======

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

>>>>>>> Stashed changes
