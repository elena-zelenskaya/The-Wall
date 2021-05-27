from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),  
    path("create-post/", views.add_post),
    path("create-comment/", views.add_comment),
    path("delete-post/<int:post_id>", views.delete_post),
    path("delete-comment/<int:comment_id>", views.delete_comment),
]
