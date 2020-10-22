from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from rush.models import Student
from .forms import StudentLoginForm, StudentRegistration

# Create your views here.
def rush(request):
    form = StudentLoginForm()
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            if (Student.objects.filter(pk=form.cleaned_data["puid"]).exists()):
                return HttpResponseRedirect(reverse('homepage',args=(form.cleaned_data["puid"],)))
            else:
                return HttpResponseRedirect(reverse('rush:student_setup', args=(form.cleaned_data["puid"],)))
    context = {
        "form":form,
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