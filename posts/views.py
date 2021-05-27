from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from datetime import datetime, timedelta
from django.utils import timezone
from users.models import User
from .models import Post, Comment

# Create your views here.
def index(request):
    if 'userid' in request.session.keys():
        context = {
			"posts": Post.objects.all().order_by("-created_at"),
			"comments": Comment.objects.all(),
		}
        return render(request, "posts/index.html", context)
    else:
        return HttpResponse("<h1>Access Denied</h1>")

def add_post(request):
    if request.method == "POST":
        post = request.POST["post_message"]
        if len(post) == 0:
            messages.error(request, "Your message is empty!", extra_tags='empty_post')
            return redirect("/wall")
        user_id = request.session["userid"]
        user = User.objects.get(id=user_id)
        Post.objects.create(post= post, user_id = user)
        # request.session["post"] = new_post.post
        return redirect("/wall")

def delete_post(request, post_id):
    if request.method == "POST":
        post_to_delete = Post.objects.get(id=post_id)
        if post_to_delete.user_id.id == request.session["userid"] and post_to_delete.created_at + timedelta(minutes=30 ) >= timezone.now(): 
            post_to_delete.delete()
        elif post_to_delete.created_at + timedelta(minutes=30 ) < timezone.now():
            messages.error(request, "This message is too old to delete", extra_tags='denied_post')
        else:
            messages.error(request, "You can't delete this message", extra_tags='denied_post')
        return redirect("/wall")

def add_comment(request):
    if request.method == "POST":
        comment = request.POST["post_comment"]
        if len(comment) == 0:
            messages.error(request, "Your comment is empty!", extra_tags='empty_comment')
            return redirect("/wall")
        user_id = request.session["userid"]
        post_id = request.POST["postid"]
        user = User.objects.get(id=user_id)
        post = Post.objects.get(id=post_id)
        Comment.objects.create(comment = comment, user_id = user, post_id = post)
        return redirect("/wall")

def delete_comment(request, comment_id):
    if request.method == "POST":
        comment_to_delete = Comment.objects.get(id=comment_id)
        if comment_to_delete.user_id.id == request.session["userid"]:
            comment_to_delete.delete()
        else:
            messages.error(request, "You can't delete this comment", extra_tags='denied_comment')
        return redirect("/wall")
