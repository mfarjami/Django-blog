from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from blog.models import Profile
from django.views.generic import *
from .forms import *

class CreateProfilePageView(CreateView):
	model = Profile
	form_class = ProfilePageForm
	template_name = 'registration/create_user_profile.html'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class EditProfilePageView(UpdateView):
	model = Profile
	template_name = 'registration/Edit_profile_page.html'
	fields = ["bio","profile_pic","facebook_url","twitter_url","instagram_url","telegram_url"]
	success_url = reverse_lazy('blog:home')


class ShowProfilePageView(DetailView):
	model = Profile
	template_name = 'registration/user_profile.html'


	def get_context_data(self, *args, **kwargs):
		# users = Profile.objects.all()
		context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
		page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
		context["page_user"]= page_user
		return context



class PassworfChangeView(PasswordChangeView):
	form_class = ChangePasswordForm
	success_url = reverse_lazy('blog:password_success')


def password_success(request):
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