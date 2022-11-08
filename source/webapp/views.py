from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import ToDo, STATUS_CHOICES

# Create your views here.


def index_views(request):
    todos = ToDo.objects.order_by('-started')
    context = {
        'todos': todos
    }
    return render(request, "index.html", context)


def info_views(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    context = {'todo': todo}
    return render(request, 'info.html', context)


def add_views(request):
    if request.method == "GET":
        return render(request, "add.html", {'choice': STATUS_CHOICES})
    elif request.method == "POST":
        goal = request.POST.get('goal')
        content = request.POST.get('content')
        started = request.POST.get('started')
        choice = request.POST.get('choice')
        new_todo = ToDo.objects.create(goal=goal, content=content, started=started, choice=choice)
        return redirect('info', pk=new_todo.pk)
