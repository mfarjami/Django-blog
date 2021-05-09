from django.urls import path
from .views import *

app_name='account'

urlpatterns = [
	path('register/',UserRegisterView.as_view(),name='register'),
	path('edit_profile/',UserEditView.as_view(),name='edit_profile'),
	path('password/',PassworfChangeView.as_view(template_name='registration/change_password.html')),
]