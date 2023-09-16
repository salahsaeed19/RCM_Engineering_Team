from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('add_post/', views.add_post, name='add_post'),
    path('search/', views.search_posts, name='search_posts'),
    path('category/<int:category_id>/', views.filter_posts_by_category, name='filter_posts_by_category'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
]
