from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import ToDo, STATUS_CHOICES
from webapp.forms import ToDoForm
# Create your views here.


def index_views(request):
    todos = ToDo.objects.order_by('-started')
    return render(request, "index.html", {'todos': todos})


def info_views(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    context = {'todo': todo}
    return render(request, 'info.html', context)


def add_views(request):
    if request.method == "GET":
        form = ToDoForm()
        return render(request, "add.html", {'form': form, 'choice': STATUS_CHOICES})
    elif request.method == "POST":
        form = ToDoForm(data=request.POST)
        if form.is_valid():
            new_todo = ToDo.objects.create(
                goal=form.cleaned_data['goal'],
                content=form.cleaned_data['content'],
                deadline=form.cleaned_data['deadline']
            )
            return redirect('info', pk=new_todo.pk)
        else:
            return render(request, 'add.html', {'form': form, 'choice': STATUS_CHOICES})


def updated_view(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    if request.method == 'GET':
        form = ToDoForm(initial={'goal': todo.goal, 'content': todo.content, 'deadline': todo.deadline})
        return render(request, 'updated.html', {'form': form, 'choice': STATUS_CHOICES})
    elif request.method == "POST":
        form = ToDoForm(data=request.POST)
        if form.is_valid():
            todo.goal = form.cleaned_data.get['goal']
            todo.content = form.cleaned_data.get['content']
            todo.deadline = form.cleaned_data['deadline']
            todo.save()
            return redirect('info', pk=todo.pk)
        else:
            return render(request, 'updated.html', {'choice': STATUS_CHOICES, 'form': form})


def delete_view(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'todo': todo})
    elif request.method == 'POST':
        todo.delete()
        return redirect('index')