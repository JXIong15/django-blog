from django.shortcuts import render
from .models import Post
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import PostCreateForm, PostUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

class SignUp(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/signup.html"

@login_required
def index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})

@login_required
def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'post/post.html', {'post': post})

class PostCreate(LoginRequiredMixin, CreateView):
  model = Post
  template_name = "post/post_create_form.html"
  form_class = PostCreateForm

class PostUpdate(LoginRequiredMixin, UpdateView):
  model = Post
  template_name = "post/post_update_form.html"
  form_class = PostUpdateForm

class PostDelete(LoginRequiredMixin, DeleteView):
  model = Post
  template_name = "post/post_delete_form.html"
  success_url = "/"

def logout_request(request):
  logout(request)
  return redirect("index")