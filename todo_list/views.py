from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def index(request):
    # session uses to check if the variable is already exist in the browser (only visibale on same session / like session storage in html)
    if "todo_list_items" not in request.session:
        request.session["todo_list_items"] = []

    return render(request, 'todo_list/index.html', {
        "tasks" : request.session["todo_list_items"]
    })


# class to represent form from django
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New item")


def add(request):
    if request.method == 'POST':
        # above if is true we are storing all the post data into form variable
        form = NewTaskForm(request.POST)
        if form.is_valid():
            # task is the data in above class i.e; the form data
            task_created = form.cleaned_data["task"]
            request.session["todo_list_items"] += [task_created]
            return HttpResponseRedirect(reverse("todo:index"))
        else:
            return render(request, 'todo_list/add.html', {
                #have to send existing form data
                "form": form
            })

    return render(request, 'todo_list/add.html', {
        'form': NewTaskForm()
    })