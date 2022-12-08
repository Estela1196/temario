from django.shortcuts import render, redirect
#from .forms import AgregarTarea

tareas = []

def home(request):
	context = {'tareas' : tareas}
	return render(request, "todo/home.html", context)

def add(request):
#	if request.method == 'POST':
#		form = AgregarTarea(request.POST)
#		if form.is_valid():
#			tarea = form.cleaned_data["tarea"]
#			tareas.append(tarea)
#			return redirect('home')
		
#	else: 
#		form = AgregarTarea()

#	context = {'form' : form}
	return render(request, "todo/add.html")

def sub1(request):
	return render(request, "todo/sub1.html")
	
def sub2(request):
	return render(request, "todo/sub2.html")	

def sub3(request):
	return render(request, "todo/sub3.html")
	
def sub4(request):
	return render(request, "todo/sub4.html")
	
def sub5(request):
	return render(request, "todo/sub5.html")
	
def sub6(request):
	return render(request, "todo/sub6.html")
	
def sub7(request):
	return render(request, "todo/sub7.html")
