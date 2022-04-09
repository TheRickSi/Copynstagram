"""Users views."""

# Django
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView
# Exception

# Models

from users.forms import SignupForm
from users.models import Profile
from django.contrib.auth.models import User
from posts.models import Post

class UserDetailView(LoginRequiredMixin,DetailView):
    template_name='users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset= User.objects.all()
    context_object_name='user'

    def get_context_data(self, **kwargs):
        """Add user's post to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


class LogginView(auth_views.LoginView):
    """Login View."""
    template_name='users/login.html'
    redirect_authenticated_user = True

class SignupView(FormView):
    template_name = "users/signup.html"
    form_class = SignupForm
    success_url = reverse_lazy("users:login")
    redirect_authenticated_user = True
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class LogoutView(auth_views.LogoutView,LoginRequiredMixin):
    """Logout view."""
    next_page = reverse_lazy("users:login")



class UpdateProfileView(LoginRequiredMixin,UpdateView):
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']
    template_name = "users/update_profile.html"
    def get_object(self,queryset=None):
        return self.request.user.profile

    def get_success_url(self):
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username':username})