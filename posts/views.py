"""Posts views."""

# Django
import profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

# Utilities
from datetime import datetime
from posts.forms import PostForm
from posts.models import Post



class PostDetailView(LoginRequiredMixin, DetailView):
    template_name="posts/detail.html"
    queryset= Post.objects.all()
    context_object_name = 'post'

class PostListView(LoginRequiredMixin, ListView):
    template_name = "posts/feed.html"
    model = Post
    ordering = ('-created',)
    paginate_by = 4
    context_object_name ='posts'


class CreatePostView(LoginRequiredMixin,CreateView):
    template_name= "posts/new.html"
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        
        context =super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context

