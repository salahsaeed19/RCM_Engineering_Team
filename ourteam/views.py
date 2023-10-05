from django.shortcuts import render, get_object_or_404, redirect
from .models import TeamMember


def team_list(request):
    team_members = TeamMember.objects.all()
    return render(request, 'ourteam/team_list.html', {'team_members': team_members})


def salah(request):
    return render(request, 'ourteam/salah.html')


# def team_member_detail(request, member_id):
#     team_member = get_object_or_404(TeamMember, pk=member_id)
#     return render(request, 'ourteam/team_member_detail.html', {'team_member': team_member})