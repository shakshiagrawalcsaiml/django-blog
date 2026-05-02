from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post
from django.shortcuts import get_object_or_404



def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        User.objects.create_user(username=username, password=password)
        return redirect('/login/')

    return render(request, 'signup.html')


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def create_post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')

        Post.objects.create(
            title=title,
            content=content,
            image=image,
            author=request.user
        )
        return redirect('/')

    return render(request, 'create_post.html')




def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post_detail.html', {'post': post})
def logout_view(request):
    logout(request)
    return redirect('/')


@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)

    # Only allow author to delete
    if post.author == request.user:
        post.delete()

    return redirect('/')