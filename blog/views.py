from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreatePostForm, UpdatePostForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Post
from django.core.paginator import Paginator


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
    posts_list = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts_list, 9)  # Show 9 posts per page
    page_number = request.GET.get('page')  # Get the page number from the query parameter
    posts = paginator.get_page(page_number)  # Get the posts for the current page
    context = {'posts': posts}
    return render(request, 'blog/posts.html', context=context)


@login_required(login_url='login')
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context=context)

@login_required(login_url='login')
def create_post(request):

    form = CreatePostForm()

    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # Don't save to the database yet
            post.published_by = request.user  # Assign the logged-in user
            post.save()  # Save to the database
            return redirect("posts")

    context = {'form': form}
    return render(request, 'blog/create_post.html', context=context)


@login_required(login_url='login')
def update_post(request, pk):

    post = Post.objects.get(id=pk)
    form = UpdatePostForm(instance=post)

    if request.method == "POST":
        form = UpdatePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("posts")

    context = {'form': form}
    return render(request, 'blog/update_post.html', context=context)