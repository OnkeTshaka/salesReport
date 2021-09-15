from django.shortcuts import render,redirect
from .models import Profile
from .forms import ProfileForm,UserForm

from django.contrib.auth.decorators import login_required

@login_required
def updateProfile(request):
	customer = Profile.objects.get(user=request.user)
	user = request.user
	profile = user.profile
	form = ProfileForm(instance=profile)
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=user)
		if user_form.is_valid():
			user_form.save()

		form = ProfileForm(request.POST, request.FILES, instance=profile)
		if form.is_valid():
			form.save()
			return redirect('/')


	context = {'form':form,'profile':customer}
	return render(request, 'profiles/main.html', context)