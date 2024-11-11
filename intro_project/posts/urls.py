"""
Url fil
"""
from django.urls import path
from . import views

urlpatterns = [
<<<<<<< Updated upstream
    path("", views.index, name="index"),
=======
    path('admin/', admin.site.urls),
    path("", views.index, name="index"), #home page
    path('create_post/', views.create_post, name='create_post'),
    #path('create_posts/', views.create_post, name='create_posts'),

>>>>>>> Stashed changes
]
