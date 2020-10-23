from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from rush.models import Student, Fraternity
from .forms import StudentLoginForm, StudentRegistration, FraternityLogin, FraternityRegistration

# Create your views here.
def rush(request):
    form = StudentLoginForm()
    form2 = FraternityLogin()
    if request.method == 'POST':
        if (request.POST.get("puid")):
            form = StudentLoginForm(request.POST)
            if form.is_valid():
                if (Student.objects.filter(pk=form.cleaned_data["puid"]).exists()):
                    return HttpResponseRedirect(reverse('rush:homepage',args=(form.cleaned_data["puid"],)))
                else:
                    return HttpResponseRedirect(reverse('rush:student_setup', args=(form.cleaned_data["puid"],)))
        if (request.POST.get("Email")):
            form = FraternityLogin(request.POST)
            if form.is_valid():
                if (Fraternity.objects.filter(email=form.cleaned_data["Email"],password=form.cleaned_data["Password"]).exists()):
                    return HttpResponseRedirect(reverse('rush:fraternity_home',args=(Fraternity.objects.get(email=form.cleaned_data["Email"]).id,)))
    context = {
        "form":form,
        "form2": form2,
    }
    return render(request, 'start_screen.html', context)

def setup(request, pk):
    form = StudentRegistration()
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            student = Student(
                puid = pk,
                name = form.cleaned_data["Name"],
                email = form.cleaned_data["Email"],
                phone = form.cleaned_data["Phone"],
                major = form.cleaned_data["Major"],
                gpa = form.cleaned_data["GPA"],
                hometown = form.cleaned_data["Hometown"],
                grade = form.cleaned_data["Grade"]
            )
            student.save()
            return HttpResponseRedirect(reverse('rush:homepage',args=(pk,)))
    context = {
        "form":form,
        "pk":pk,
    }
    return render(request, 'student_setup.html', context)

def home(request, pk):
    form = StudentRegistration()
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            student = Student(
                puid = pk,
                name = form.cleaned_data["Name"],
                email = form.cleaned_data["Email"],
                phone = form.cleaned_data["Phone"],
                major = form.cleaned_data["Major"],
                gpa = form.cleaned_data["GPA"],
                hometown = form.cleaned_data["Hometown"],
                grade = form.cleaned_data["Grade"]
            )
            student.save()
    context = {
        "form":form,
        "pk":pk,
        "student":student,
    }
    return render(request, 'homepage.html', context)

def fraternitySetup(request):
    form = FraternityRegistration()
    if request.method == 'POST':
        form = FraternityRegistration(request.POST)
        if form.is_valid():
            fraternity = Fraternity(
                name = form.cleaned_data["Name"],
                email = form.cleaned_data["Email"],
                password = form.cleaned_data["Password"]
            )
            fraternity.save()
            
    context = {
        "form":form,
    }
    return render(request, 'fraternity_setup.html', context)
def fraternityHome(request, pk):
    fraternity = Fraternity.objects.get(id=pk)
    context = {
        "fraternity":fraternity,
    }
    return render(request, 'fraternity_home.html', context)