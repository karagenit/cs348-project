from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from rush.models import Student, Fraternity, Event
from .forms import StudentLoginForm, StudentRegistration, FraternityLogin, FraternityRegistration, EventRegistration

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
    student = Student.objects.get(pk=pk)
    fraternities = Fraternity.objects.exclude(applicants=student)
    applied = Fraternity.objects.filter(applicants=student)
    events = Event.objects.filter(attendees=student)
    context = {
        "pk":pk,
        "student":student,
        "fraternities":fraternities,
        "applied":applied,
        "events":events,
    }
    return render(request, 'homepage.html', context)

def studentBrief(request, pk, puid):
    student = Student.objects.get(puid=puid)
    fraternity = Fraternity.objects.get(id=pk)
    attended = Event.objects.filter(host=fraternity, attendees=student)
    context = {
        "student":student,
        "id":pk,
        "attended":attended,
    }
    return render(request, 'student.html', context)

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
            new = Fraternity.objects.get(email = fraternity.email)
            return HttpResponseRedirect(reverse('rush:fraternity_home', args=(new.id,)))
    context = {
        "form":form,
    }
    return render(request, 'fraternity_setup.html', context)
def fraternityHome(request, pk):
    fraternity = Fraternity.objects.get(id=pk)
    events = Event.objects.filter(host=(Fraternity.objects.get(id=pk)))
    applicants = fraternity.applicants.all()
    context = {
        "fraternity":fraternity,
        "id":pk,
        "events":events,
        "applicants": applicants,
    }
    return render(request, 'fraternity_home.html', context)

def fraternity(request, student, pk):
    fraternity = Fraternity.objects.get(id=pk)
    print(fraternity.applicants)
    student1 = Student.objects.get(puid=student)
    if request.method == 'POST':
        fraternity.applicants.add(student1)
        return HttpResponseRedirect(reverse('rush:homepage',args=(student1.puid,)))
    context = {
        "fraternity": fraternity,
    }
    return render(request, 'fraternity.html', context)

def fraternityBrief(request, pk, id):
    fraternity = Fraternity.objects.get(id=id)
    events = Event.objects.filter(host=fraternity)
    context = {
        "fraternity": fraternity,
        "events": events,
        "id":pk,
    }
    return render(request, 'fraternity_brief.html', context)

def eventSetup(request, pk):
    form = EventRegistration()
    fraternity = Fraternity.objects.get(id=pk)
    if request.method == 'POST':
        form = EventRegistration(request.POST)
        if form.is_valid():
            event = Event(
                name = form.cleaned_data["Name"],
                date = form.cleaned_data["Date"],
                host = fraternity
            )
            event.save()
            return HttpResponseRedirect(reverse('rush:fraternity_home', args=(pk,)))
    context = {
        "form":form,
    }
    return render(request, 'event_setup.html', context)

def event(request, pk, id):
    event = Event.objects.get(id=id)
    students = event.attendees
    context = {
        "event":event,
        "students":students.all(),
        "id":pk,
    }
    return render(request, 'event.html',context)

def eventBrief(request, pk, fid, event):
    event = Event.objects.get(id=event)
    student = Student.objects.get(puid=pk)
    if request.method == 'POST':
        event.attendees.add(student)
        return HttpResponseRedirect(reverse('rush:homepage',args=(pk,)))
    context = {
        "event":event,
        "fratId": fid,
        "id":pk,
    }
    return render(request, 'event_brief.html', context)