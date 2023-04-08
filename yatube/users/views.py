from django.views.generic import CreateView

from django.urls import reverse_lazy

from .forms import CreationForm, PostForm

class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'

class PostCreate(CreateView):
    form_class = PostForm
    success_url = reverse_lazy('posts:profile')
    template_name = 'posts/create_post.html'
