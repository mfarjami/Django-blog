from django.urls import path
from .views import *

app_name='account'

urlpatterns = [
	path('register/',UserRegisterView.as_view(),name='register'),
	path('edit_profile/',UserEditView.as_view(),name='edit_profile'),
	path('password/',PassworfChangeView.as_view(template_name='registration/change_password.html')),
	path('password_succes', password_success, name='password_success'),
	path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile'),
	path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
	path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),
]