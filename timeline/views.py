from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from timeline.models import Post, Like


def login_user(request):
    if request.method == 'POST':
        username, password = request.POST.get("username"), request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect('/')
    return render(request, 'login.html')


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login')


@login_required
def index(request):
    return render(request, 'index.html', {
        "all_posts": Post.objects.all().order_by('id'),
        "likes": [like.post_id for like in Like.objects.filter(liked_by__id=request.user.id)]
    })


@login_required
def like_post(request, post_id):
    if Like.objects.filter(post_id=post_id, liked_by_id=request.user.id).exists():
        Like.objects.filter(post_id=post_id, liked_by_id=request.user.id).delete()
        return JsonResponse({"message": "Post disliked", "link": "I like This"})
    Like.objects.create(post_id=post_id, liked_by_id=request.user.id)
    return JsonResponse({"message": "Post Liked!", "link": "I Dislike this"})


