from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import StudentForm
from .models import student
from django.urls import reverse
def student_management(request):
    return render(request, 'index.html', {
        'student': student.objects.all()
    })

def view_student(request, id):
    students = student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))


def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student = form.save(commit=False)  # Create a new student object from the form data
            new_student.save()  # Save the new student to the database
            return render(request, 'add.html', {'form': StudentForm(), 'success': True})
    else:
        form = StudentForm()

    return render(request, 'add.html', {'form': form})


def edit(request, id):
    std = student.objects.get(pk=id)
    if request.method == 'POST':
        forms = StudentForm(request.POST, instance=std)
        if forms.is_valid():
            forms.save()
            return render(request, 'edit.html', {'form': forms, 'success': True})
    else:
        forms = StudentForm(instance=std)

    return render(request, 'edit.html', {'form': forms})


def delete(request, id):
    std = student.objects.get(pk=id)
    if request.method == 'POST':
        std.delete()
        return HttpResponseRedirect(reverse('index'))
    return HttpResponseRedirect(reverse('index'))