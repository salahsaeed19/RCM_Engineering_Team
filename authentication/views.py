from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm, ProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            identifier = form.cleaned_data.get("identifier")
            password = form.cleaned_data.get("password")
            
            try:
                user = User.objects.get(email=identifier)
                username = user.username
            except User.DoesNotExist:
                username = identifier
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid username/email or password'
        else:
            msg = 'Error validating the form'
    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def signup(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True
            login(request, user)
            return redirect('home')
        else:
            msg = ' '.join([str(e) for e in form.errors.values()])

    else:
        form = SignUpForm()

    return render(request, "accounts/signup.html", {"form": form, "msg": msg, "success": success})


@login_required
def profile_view(request, user_id):
    profile = get_object_or_404(Profile, user_id=user_id)

    is_own_profile = request.user == profile.user

    if request.method == 'POST' and is_own_profile:
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect('profile', user_id=user_id)
        else:
            messages.error(request, "There was an error updating your profile. Please try again.")
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'accounts/profile.html', {
        'profile': profile,
        'form': form,
        'is_own_profile': is_own_profile
    })