from django.urls import path
from . import views

urlpatterns = [
    path('', views.page1, name='home'),
    path('post/<int:post_id>/', views.view_post, name='view_post'),
    path('post/create/', views.create_post, name='create_post'),
    path('post/edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('post/delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('post/<int:post_id>/add_comment/',views.comment_post,name='add_comment'),
    path('page1/',views.page1, name='latest_post'),
]
