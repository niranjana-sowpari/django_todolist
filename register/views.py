from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm

# Create your views here.

def register(response):
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()
		else:
			return HttpResponse("<h1>INVALID CREDENTIALS</h1>")

		return redirect("/")

	form = RegisterForm()
	return render(response, "register/register.html", {"form":form})
