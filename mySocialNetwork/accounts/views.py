from django.shortcuts import render
from django.views.generic import CreateView

# reverse_lazy assign that if someone loggedin and out, where he should go?
from django.urls import reverse_lazy


from . import forms



# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'