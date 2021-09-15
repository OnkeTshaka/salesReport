from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
def logout_view(request):
    logout(request)
    return redirect('login')


def registerPage(request):
	form = CustomUserCreationForm()
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.save()
			messages.success(request, 'Account successfuly created!')

			user = authenticate(request, username=user.username, password=request.POST['password1'])

			if user is not None:
				login(request, user)

			next_url = request.GET.get('next')
			if next_url == '' or next_url == None:
				next_url = 'login'
			return redirect(next_url)
		else:
			messages.error(request, 'An error has occured with registration')
	context = {'form':form}
	return render(request, 'auth/register.html', context)


def login_view(request):
    error_message = None
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('sales:home')
        else:
            error_message = 'Ups ... something went wrong'

    context = {
        'form': form,
        'error_message': error_message
    }

    return render(request, 'auth/login.html', context)