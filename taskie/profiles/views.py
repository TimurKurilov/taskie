from .models import Profile
from .forms import ProfileForm
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib import messages

def profile(request, username):
    user = User.objects.get(username=username)
    user_profile, created = Profile.objects.get_or_create(user=user)
    return render(request, "profiles/profile.html", {"user": user, "user_profile": user_profile})

def edit_profile(request, username):
    user = get_object_or_404(User, username=username)
    user_profile = get_object_or_404(Profile, user=user)

    if request.user != user_profile.user:
        return render(request, "profiles/access_denied.html")
    
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль успешно обновлен")
            return redirect(f'/profile/{username}/')
        else:
            messages.error(request, "Пожалуйста, исправьте ошибки в форме")
    else:
        form = ProfileForm(instance=user_profile)
    
    return render(request, "profiles/edit_profile.html", {
        "form": form, 
        "username": username
    })