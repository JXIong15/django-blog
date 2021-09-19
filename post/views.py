from django.shortcuts import render
from .models import Post
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import PostCreateForm, PostUpdateForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})

def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'post/post.html', {'post': post})

class PostCreate(CreateView):
  model = Post
  template_name = "post/post_create_form.html"
  form_class = PostCreateForm

class PostUpdate(UpdateView):
  model = Post
  template_name = "post/post_update_form.html"
  form_class = PostUpdateForm

class PostDelete(DeleteView):
  model = Post
  template_name = "post/post_delete_form.html"
  success_url = "/"