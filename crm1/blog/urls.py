from django.urls import path
from .views import *

app_name= 'blog'

urlpatterns = [
	path('',PostList.as_view(),name='home'),
	path('detail/<int:pk>/',PostDetail.as_view(),name='detail'),
	path('create/',PostCreate.as_view(),name='create'),
	path('category/',PostCategoryView.as_view(),name='category'),
	path('update/<int:pk>/',PostUpdate.as_view(),name='update'),
	path('delete/<int:pk>/',PostDelete.as_view(),name='delete'),
	path('category/<str:cats>/', CategoryView, name='categories'),
	path('category-list/', CategoryListView, name='category-list'),
	path('like/<int:pk>', LikeView, name='like_post'),
]