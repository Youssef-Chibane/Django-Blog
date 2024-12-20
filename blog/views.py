from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Post


def home(request):
    posts = Post.objects.all().order_by('-created_at')[:6]
    context = {'posts': posts}
    return render(request, 'blog/home.html', context=context)


def signup(request):
    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    context = {'form':form}
    return render(request, 'blog/signup.html', context=context)


def login(request):
    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("home")

    context = {'form':form}

    return render(request, 'blog/login.html', context=context)


def logout(request):

    auth.logout(request)
    return redirect("home")


@login_required(login_url='login')
def posts(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {'posts': posts}
    return render(request, 'blog/posts.html', context=context)

@login_required(login_url='login')
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context=context)

