from django.urls import reverse_lazy

from django.views import generic

from .forms import CustomUserCreationForm

class SignupPageView(generic.CreateView):
  success_url = reverse_lazy('login')
  template_name = 'signup.html'
  form_class = CustomUserCreationForm