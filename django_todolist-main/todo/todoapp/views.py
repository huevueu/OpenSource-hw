from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    todo_items = Todo.objects.all()
    form = TodoForm()

    if request.method == 'POST':
        if 'add_todo' in request.POST:
            form = TodoForm(request.POST)
            if form.is_valid():
                new_todo = Todo(title=form.cleaned_data['text'])
                new_todo.save()
                return redirect('todo_list')
        
    todo_items = Todo.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todo_items, 'form': form})
