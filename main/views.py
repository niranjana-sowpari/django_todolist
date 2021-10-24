from django.shortcuts import render, redirect
from django.http import HttpResponse

from . models import ToDoList, Item
from . forms import ShowList

# Create your views here.

def index(response, id):
	ls = ToDoList.objects.get(id=id)
	#itemi = ls.item_set.get(id=1)
	#return HttpResponse("<h1>{}</h1>".format(ls.name))

	if ls in response.user.todolist.all():

		if response.method == "POST":
			print(response.POST)
			if response.POST.get("save"):
				for item in ls.item_set.all() :
					if response.POST.get("c" + str(item.id)):
						item.complete = True
					else:
						item.complete = False

					print("***********\n ",item.complete)
					item.save()

			elif response.POST.get("add"):
				txt = response.POST.get("new")

				if len(txt)>2:
					ls.item_set.create(text=txt,complete=False)
				else:
					print("invalid")


		return render(response,"main/list.html",{"ls":ls})

	else:
		return redirect("/view")


def home(response):
	return render(response,"main/home.html",{})

def create(response):
	if response.method == "POST":
		form = ShowList(response.POST)

		if form.is_valid():
			n = form.cleaned_data["name"]
			#response.user.todolist_set.create(name=n)
			t = ToDoList(name=n)
			t.save()
			response.user.todolist.add(t)

	form = ShowList()
	return render(response,"main/create.html",{"form":form})

def view(response):
	return render(response,"main/view.html",{})