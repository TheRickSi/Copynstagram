"""Copygram Middleware catalog."""

#Django
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:
    """Profile completion middleware.
    ensure every user that isinteracting with the
    platform have their progile picture and
    biography.
    """
    def __init__(self,get_response):
        """middleware initizlization"""
        self.get_response=get_response
        
    def __call__(self,request):
        """Code to  be execute for each request
        before the view is called."""
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile= request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('updateProfile'),reverse('logout')]:
                        return redirect('updateProfile')
        response= self.get_response(request)
        return response