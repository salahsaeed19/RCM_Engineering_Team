from django.urls import path
from ourteam import views

urlpatterns = [
    path('ourteam/', views.team_list, name='team_list'),
    path('ourteam/<int:member_id>/', views.team_member_detail, name='team_member_detail'),
    # Add URLs for adding, editing, and deleting team members as needed.
]