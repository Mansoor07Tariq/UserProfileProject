from django.shortcuts import render, redirect
from .forms import UserProfileForm

def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_created')
    else:
        form = UserProfileForm()

    return render(request, 'user_profile/create_profile.html', {'form': form})

def profile_created(request):
    return render(request, 'user_profile/profile_created.html')
