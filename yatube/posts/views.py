from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Post, Group, User
from .forms import PostForm
from .utils import paginator

POST_SEARCH = 10


def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    page_obj = paginator(post_list, POST_SEARCH, request)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = Post.objects.select_related('author', 'group')
    page_obj = paginator(post_list, POST_SEARCH, request)
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    post_list = Post.objects.filter(author=author)
    count_posts = Post.objects.filter(author=author).count()
    page_obj = paginator(post_list, POST_SEARCH, request)
    context = {
        'count_posts': count_posts,
        'author': author,
        'page_obj': page_obj,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    count_posts = Post.objects.filter(author=post_id).count()
    context = {
        'count_posts': count_posts,
        'post': post,
    }
    return render(request, "posts/post_detail.html", context)


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:profile', post.author)
        return render(request, "posts/create_post.html", {'form': form})
    form = PostForm()
    return render(request, "posts/create_post.html", {'form': form})


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user:
        return redirect(f'/profile/{post.author}')
    
    if request.method == 'POST':
        form = PostForm(request.POST or None, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('posts:post_detail', post_id)

    else:
        form = PostForm(instance=post)
        context = {
            'post': post,
            'is_edit': True,
            'form': form,
            'post_id': post_id,
        }
        return render(request, "posts/create_post.html", context)
    return render(request, "posts/create_post.html", context)
