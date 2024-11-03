from django.urls import path
from . import views

urlpatterns = [
    path('', views.summary_list, name='summary_list'),
    path('search_summaries/', views.search_summaries, name='search_summaries'),
    path('category/<str:category>/', views.filter_summaries_by_category, name='filter_summaries_by_category'),
    path('summary/increment_views/<int:summary_id>/', views.increment_views_and_redirect, name='increment_views_and_redirect'),
    # path('summary/<int:summary_id>/', views.summary_detail, name='summary_detail'),
    # path('add_summary/', views.add_summary, name='add_summary'),
    # path('edit_summary/<int:summary_id>/', views.edit_summary, name='edit_summary'),
]