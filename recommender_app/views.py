from django.shortcuts import render,get_object_or_404,redirect
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views import generic
from .models import *
from .forms import CreateUserForm,CreateProfileForm,RateForm

# Create your views here.
def SignUpView(request):
	form=CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + username)
			return redirect('login')
	context = {'form':form}
	return render(request, 'signup.html', context)

def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')
		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


def home(request):
	return render(request ,"/",context)


'''def CreateProfile(request):
		form = CreateProfileForm()
		if request.method == 'POST':
				#print("printing",request.POST)
				form = CreateProfileForm(request.POST)
				if form.is_valid():
					form.save()
					return redirect('/')
		return render(request, 'createprofile.html', {'form': form})'''

def EditProfile(request,pk_test):
	student=get_object_or_404(Student,id=pk_test)
	form = CreateProfileForm(instance=student)
	if request.method == 'POST':
		form = CreateProfileForm(request.POST,instance=student)
		if form.is_valid():
			form.save()
			return redirect('/')
					
	return render(request, 'editprofile.html', {'student.id': student.id})

def CourseList(request):
	course_list=Course.objects.all()[:20]

	'''form=RateForm()
	if request.method == 'POST':
		#print("printing",student.id,course.id,request.POST)
		form = RateForm(request.POST)
		if form.is_valid():
			form.save()'''
	context={'course_list':course_list}
	return render(request,'courselist.html',context)


def Rate(request,course_id):
	if not request.user.is_authenticated:
		return redirect("login")
	form=RateForm()
	course = get_object_or_404(Course,id=course_id)

	if request.method == "POST":
		print(request.POST)
		rate = request.POST['rating']
		ratingObject = Rating()
		ratingObject.student_id   = request.user.student
		ratingObject.course_id  = course
		ratingObject.rating = rate
		ratingObject.save()
		messages.success(request,"Your Rating is submited ")
		return redirect("courselist")
	return render(request,'rate.html',{'course':course,'form':form})