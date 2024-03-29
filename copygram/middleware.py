"""platzigram middleware catalog"""
#django
from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
  """Profile completion middleware
  Ensure every user is interacting with the 
  platform have their profile picture and biography
  """
  def __init__(self,get_response):
    """Middleware initialization"""
    self.get_response= get_response

  def __call__(self,request):
    """Code to be executed for each request before the view is called"""
    if not request.user.is_anonymous:
        if not request.user.is_staff:
            profile = request.user.profile
            if not profile.biography:
                if request.path !=  reverse('users:update_profile'):
                    return redirect('users:update_profile')

    response= self.get_response(request)
    return response
  
class SignupAlreadyMiddleware:
  "Signup protection when the user already logged"
  
  def __init__(self, get_response):
      self.get_response = get_response
    
  def __call__(self, request):
    if not request.user.is_anonymous:
      if request.path == reverse('users:signup'):
        return redirect('posts:feed')
    response = self.get_response(request)
    return response