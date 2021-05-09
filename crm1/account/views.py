from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import *
from .forms import *

class PassworfChangeView(PasswordChangeView):
	form_class = ChangePasswordForm
	success_url = reverse_lazy('blog:password_success')

def password_success(requesst):
	return render(request, 'registration/password_success.html')

class UserRegisterView(CreateView):
	form_class = SignUpForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')

class UserEditView(UpdateView):
	form_class = EditProfileForm
	template_name = 'registration/edit_profile.html'
	success_url = reverse_lazy('blog:home')

	def get_object(self):
		return self.request.user