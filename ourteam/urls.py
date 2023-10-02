from django.urls import path
from ourteam import views

urlpatterns = [
    path('ourteam/', views.team_list, name='team_list'),
    # path('ourteam/<int:member_id>/', views.team_member_detail, name='team_member_detail'),
    path('ourteam/salah/', views.salah, name='salah'),
]
