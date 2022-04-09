"""Platzigram URLs module."""

# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include


from posts import views as posts_views
from users import views as users_views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('admin/', admin.site.urls),

    path('',include(('posts.urls','posts') , namespace = 'posts')),

    path('users/',include(('users.urls','users'), namespace= 'users'))


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
